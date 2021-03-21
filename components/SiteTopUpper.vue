<template>
  <div class="MainPage">
    <div class="Header mb-3">
      <page-header :icon-path="headerItem.iconPath">
        {{ headerItem.title }}
      </page-header>
      <div class="UpdatedAt">
        <span>{{ $t('最終更新') }}</span>
        <time :datetime="updatedAt">{{ formattedDateForDisplay }}</time>
      </div>
      <div v-show="!['ja', 'ja-basic'].includes($i18n.locale)" class="Annotation">
        <span>{{ $t('注釈') }}</span>
      </div>
    </div>
    <whats-new :items="newsItems" :is-emergency="false" />
    <div class="row mt-3">
      <staying-population />
      <consultation />
      <patients-summary-card />
      <patients-number-card />
    </div>
  </div>
</template>

<script lang="ts">
import { mdiChartTimelineVariant } from '@mdi/js'
import Vue from 'vue'
import { MetaInfo } from 'vue-meta'

import Data from '@/data/data.json'
import News from '@/data/news.json'
import { convertDatetimeToISO8601Format } from '@/utils/formatDate'

const PageHeader = () => import('@/components/PageHeader.vue')
// 最新のお知らせ
const WhatsNew = () => import('@/components/WhatsNew.vue')
// 滞在人口
const StayingPopulation = () => import('@/components/StayingPopulation.vue')
// 電話相談
const Consultation = () => import('@/components/Consultation.vue')
// 検査陽性者の状況
const PatientsSummaryCard = () => import('@/components/cards/PatientsSummaryCard.vue')
// 公表日別による陽性者数の推移
const PatientsNumberCard = () => import('@/components/cards/PatientsNumberCard.vue')

export default Vue.extend({
  components: {
    PageHeader,
    WhatsNew,
    StayingPopulation,
    Consultation,
    PatientsSummaryCard,
    PatientsNumberCard,
  },
  data() {
    const { lastUpdate } = Data

    return {
      headerItem: {
        iconPath: mdiChartTimelineVariant,
        title: this.$t('県内の最新感染動向'),
      },
      lastUpdate,
      newsItems: News.newsItems,
    }
  },
  computed: {
    updatedAt() {
      return convertDatetimeToISO8601Format(this.$data.lastUpdate)
    },
    formattedDateForDisplay() {
      return `${this.$d(new Date(this.$data.lastUpdate), 'dateTime')} JST`
    },
  },
  head(): MetaInfo {
    return {
      title: this.$t('県内の最新感染動向') as string,
    }
  },
})
</script>

<style lang="scss" scoped>
.MainPage {
  .Header {
    display: flex;
    flex-wrap: wrap;
    align-items: flex-end;

    @include lessThan($small) {
      flex-direction: column;
      align-items: baseline;
    }
  }

  .UpdatedAt {
    @include font-size(14);

    color: $gray-3;
    margin-bottom: 0.2rem;
  }

  .Annotation {
    @include font-size(12);

    color: $gray-3;
    @include largerThan($small) {
      margin: 0 0 0 auto;
    }
  }
}
</style>
