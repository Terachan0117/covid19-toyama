<template>
  <div class="WhatsNew">
    <div class="WhatsNew-heading">
      <h3 class="WhatsNew-title">
        <v-icon size="2.4rem" class="WhatsNew-title-icon">
          {{ mdiInformation }}
        </v-icon>
        {{ $t('最新のお知らせ') }}
      </h3>
      <div class="WhatsNew-linkGroup">
        <lazy-link-to-information-about-emergency-measure v-if="isEmergency" />
        <app-link
          class="WhatsNew-linkButton"
          to="http://www.pref.toyama.jp/cms_sec/1205/kj00023252.html"
        >
          <VaccineIcon class="WhatsNew-linkButton-icon" aria-hidden="true" />
          {{ $t('ワクチン情報') }}
        </app-link>
      </div>
    </div>
    <ul class="WhatsNew-list">
      <li v-for="(item, i) in items" :key="i" class="WhatsNew-list-item">
        <app-link :to="item.url" class="WhatsNew-list-item-anchor">
          <time
            class="WhatsNew-list-item-anchor-time px-2"
            :datetime="formattedDate(item.date)"
          >
            {{ formattedDateForDisplay(item.date) }}
          </time>
          <span class="WhatsNew-list-item-anchor-link">
            {{ item.text }}
          </span>
        </app-link>
      </li>
      <li class="WhatsNew-list-item">
        <a href="https://twitter.com/covid19_toyama" target="_blank" rel="noopener noreferrer" class="WhatsNew-list-item-anchor ExternalLink">
          <span class="WhatsNew-list-item-anchor-link">
            {{ $t('Twitterアカウント-富山県公認新型コロナ対策サイト') }}
          </span>
          <span aria-label="別タブで開く" role="img" class="v-icon notranslate ExternalLinkIcon theme--light" style="font-size:1.2rem;height:1.2rem;width:1.2rem">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" role="img" aria-hidden="true" class="v-icon__svg" style="font-size:1.2rem;height:1.2rem;width:1.2rem"><path d="M14,3V5H17.59L7.76,14.83L9.17,16.24L19,6.41V10H21V3M19,19H5V5H12V3H5C3.89,3 3,3.9 3,5V19A2,2 0 0,0 5,21H19A2,2 0 0,0 21,19V12H19V19Z"></path></svg>
          </span>
        </a>
      </li>
      <li class="WhatsNew-list-item">
        <a href="https://line.me/R/ti/p/%40925tfblm" target="_blank" rel="noopener noreferrer" class="WhatsNew-list-item-anchor ExternalLink">
          <span class="WhatsNew-list-item-anchor-link">
            {{ $t('LINEアカウント-富山県新型コロナ対策パーソナルサポート') }}
          </span>
          <span aria-label="別タブで開く" role="img" class="v-icon notranslate ExternalLinkIcon theme--light" style="font-size:1.2rem;height:1.2rem;width:1.2rem">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" role="img" aria-hidden="true" class="v-icon__svg" style="font-size:1.2rem;height:1.2rem;width:1.2rem"><path d="M14,3V5H17.59L7.76,14.83L9.17,16.24L19,6.41V10H21V3M19,19H5V5H12V3H5C3.89,3 3,3.9 3,5V19A2,2 0 0,0 5,21H19A2,2 0 0,0 21,19V12H19V19Z"></path></svg>
          </span>
        </a>
      </li>
      <li class="WhatsNew-list-item">
        <a href="https://tera-chan.com/covid19-toyama/supportnavi/" target="_blank" rel="noopener noreferrer" class="WhatsNew-list-item-anchor ExternalLink">
          <span class="WhatsNew-list-item-anchor-link">
            {{ $t('富山県 新型コロナウイルス感染症 支援情報ナビ') }}
          </span>
          <span aria-label="別タブで開く" role="img" class="v-icon notranslate ExternalLinkIcon theme--light" style="font-size:1.2rem;height:1.2rem;width:1.2rem">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" role="img" aria-hidden="true" class="v-icon__svg" style="font-size:1.2rem;height:1.2rem;width:1.2rem"><path d="M14,3V5H17.59L7.76,14.83L9.17,16.24L19,6.41V10H21V3M19,19H5V5H12V3H5C3.89,3 3,3.9 3,5V19A2,2 0 0,0 5,21H19A2,2 0 0,0 21,19V12H19V19Z"></path></svg>
          </span>
        </a>
      </li>
    </ul>
  </div>
</template>

<script lang="ts">
import { mdiInformation } from '@mdi/js'
import Vue from 'vue'

import AppLink from '@/components/AppLink.vue'
import VaccineIcon from '@/static/vaccine.svg'
import { convertDateToISO8601Format } from '@/utils/formatDate'

export default Vue.extend({
  components: {
    AppLink,
    VaccineIcon,
  },
  props: {
    items: {
      type: Array,
      required: true,
    },
    isEmergency: {
      type: Boolean,
      required: false,
      default: false,
    },
  },
  data() {
    return {
      mdiInformation,
    }
  },
  methods: {
    formattedDate(dateString: string) {
      return convertDateToISO8601Format(dateString)
    },
    formattedDateForDisplay(dateString: string) {
      return this.$d(new Date(dateString), 'date')
    },
  },
})
</script>

<style lang="scss">
.WhatsNew {
  @include card-container();

  padding: 18px;
  margin-bottom: 10px;

  .WhatsNew-heading {
    display: flex;
    align-items: center;
    flex-wrap: wrap;
    margin-bottom: 8px;

    .WhatsNew-title {
      display: flex;
      align-items: center;
      color: $gray-2;
      margin: 8px 12px 8px 0;
      @include card-h2();
      &-icon {
        margin: 3px;
      }
    }

    .WhatsNew-linkGroup {
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      justify-content: flex-end;

      @include lessThan($medium) {
        justify-content: flex-start;
      }
    }
    
    .WhatsNew-linkButton {
      @include button-text('sm');
      &-icon {
        width: 1em;
      }
    }
  }

  .WhatsNew-list {
    padding-left: 0;
    list-style-type: none;

    &-item {
      &-anchor {
        text-decoration: none;
        margin: 5px;
        @include font-size(14);

        @include lessThan($medium) {
          display: flex;
          flex-wrap: wrap;
        }

        &-time {
          flex: 0 0 90px;

          @include lessThan($medium) {
            flex: 0 0 100%;
          }

          color: $gray-1;
        }

        &-link {
          flex: 0 1 auto;

          @include text-link();

          @include lessThan($medium) {
            padding-left: 8px;
          }
        }

        &-ExternalLinkIcon {
          margin-left: 2px;
          color: $gray-3 !important;
        }
      }
    }
  }
}
</style>
