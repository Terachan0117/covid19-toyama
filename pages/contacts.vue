<template>
  <div
    class="Contacts"
    aria-labelledby="pageHeader"
    aria-describedby="contactsCardTable"
  >
    <page-header id="pageHeader" class="mb-3">
      {{ $t('お問い合わせ先一覧') }}
    </page-header>
    <div class="Contacts-Card">
      <table
        id="contactsCardTable"
        class="Contacts-Card-Table"
        v-bind="tableAttrs"
        aria-describedby="pageHeader"
      >
        <thead>
          <tr>
            <th class="text-center" scope="col">
              {{ $t('お問い合わせ内容') }}
            </th>
            <th class="text-center" scope="col">{{ $t('担当') }}</th>
            <th class="text-center tel" scope="col">{{ $t('お問い合わせ先') }}</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="content importantContact" v-bind="headingAttrs">
              {{ $t('新型コロナウイルス感染症の予防・検査・医療に関すること') }}
            </td>
            <td class="bureau importantContact">
              {{ $t('富山県 厚生部 健康課 新型コロナウイルス対策班') }}
            </td>
            <td class="tel">
              <a href="tel:076-444-2176" class="importantContact">076-444-2176</a
              ><br />
              <p class="caution">
                {{ $t('午前8時30分から午後17時15分（土日祝：午前10時から午後4時）') }}
              </p>
              <p class="caution">
                {{ $t('電話のおかけ間違いが多くなっております。発信の際は今一度電話番号をお確かめの上、お間違えのないようお願いいたします。') }}
              </p>
            </td>
          </tr>
          <tr>
            <td class="content importantContact" v-bind="headingAttrs">
              ({{ $t('外国人の方向け') }}) {{ $t('新型コロナウイルス感染症の予防・検査・医療に関すること') }}
            </td>
            <td class="bureau importantContact">
            </td>
            <td class="tel">
              <a href="http://www.pref.toyama.jp/cms_sec/1018/kj00021433.html" target="_blank" rel="noopener noreferrer" class="importantContact">{{ $t('新型コロナウイルス感染症に関する相談窓口・各種情報等') }} ({{ $t('富山県公式ホームページ') }})</a>
            </td>
          </tr>
          <tr>
            <td class="content" v-bind="headingAttrs">
              {{ $t('本サイトの管理・運営に関すること') }}
            </td>
            <td class="bureau">{{ $t('寺田 一世') }}</td>
            <td class="tel"><a href="mailto:contact&#64;tera-chan.com?subject=富山県コロナ対策サイトについて">contact[at]tera-chan.com</a><br>{{ $t('クリックでメールソフトが起動します。直接アドレスを入力される際は、[at]を@に置換してください。') }}</td>
          </tr>
          <tr>
            <td class="content" v-bind="headingAttrs">
              {{ $t('オープンデータに関すること') }}
            </td>
            <td class="bureau">{{ $t('富山県 経営管理部 情報政策課 IT推進係') }}</td>
            <td class="tel"><a href="tel:076-444-3116">076-444-3116</a></td>
          </tr>
          <tr>
            <td class="content" v-bind="headingAttrs">
              {{ $t('その他') }}
            </td>
            <td class="bureau"></td>
            <td class="tel"><a href="http://www.pref.toyama.jp/sections/1118/virus/soudan.html" target="_blank" rel="noopener noreferrer">{{ $t('相談窓口一覧') }} ({{ $t('富山県公式ホームページ') }})</a></td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script lang="ts">
import Vue from 'vue'
import { MetaInfo } from 'vue-meta'

import PageHeader from '@/components/PageHeader.vue'
import AppLink from '@/components/AppLink.vue'

export default Vue.extend({
  components: {
    PageHeader,
    AppLink,
  },
  data() {
    return {
      pc: true,
    }
  },
  computed: {
    tableAttrs(): any {
      return this.pc ? {} : { role: 'presentation' }
    },
    headingAttrs(): any {
      return this.pc ? {} : { role: 'heading', 'aria-level': '3' }
    },
  },
  mounted() {
    if (process.browser) {
      window.addEventListener('resize', this.handleResize)
      this.handleResize()
    }
  },
  destroyed() {
    if (process.browser) {
      window.removeEventListener('resize', this.handleResize)
    }
  },
  methods: {
    handleResize() {
      this.pc = window.innerWidth > 768
    },
  },
  head(): MetaInfo {
    return {
      title: this.$t('お問い合わせ先一覧') as string,
    }
  },
})
</script>

<style lang="scss">
.Contacts {
  &-Card {
    @include card-container();

    &-Table {
      width: 100%;
      border-collapse: collapse;

      th {
        padding: 1em 0;
        @include font-size(14, true);
      }

      td {
        padding: 1em 16px;
        @include font-size(14);
      }

      .importantContact {
        font-weight: 600;
        @include font-size(16, true);
      }

      .tel ul {
        list-style: none;
        padding: 0;
      }

      .tel li {
        margin: 8px 0;
      }

      @include largerThan($medium) {
        th.tel {
          width: 35%;
        }
        th,
        tr:not(:last-child) {
          border-top: none;
          border-left: none;
          border-right: none;
          border-bottom: thin solid rgba(0, 0, 0, 0.12);
        }

        tr:last-child {
          border: none;
        }
      }

      @include lessThan($medium) {
        thead {
          display: none;
        }

        tbody {
          tr {
            height: auto;

            .content {
              font-weight: 600;
              border-bottom: none !important;
              padding-top: 12px;
              padding-bottom: 8px;
            }

            .bureau {
              border-bottom: none !important;
            }

            .tel {
              padding-bottom: 12px;
            }
          }

          tr:not(:last-child) {
            border-bottom: thin solid rgba(0, 0, 0, 0.12);
          }
        }

        td {
          display: block;
        }
      }

      p.caution {
        margin: 0;
        @include font-size(12);
      }
    }
  }
}
</style>
