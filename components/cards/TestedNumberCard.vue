<template>
  <v-col cols="12" md="6" class="DataCard">
    <client-only>
      <time-stacked-bar-chart
        :title="$t('検査実施件数')"
        :title-id="'tested-number'"
        :chart-id="'tested-number'"
        :chart-data="inspectionsGraph"
        :date="date"
        :items="inspectionsItems"
        :labels="inspectionsLabels"
        :unit="$t('人')"
        :data-labels="inspectionsDataLabels"
        :table-labels="inspectionsTableLabels"
        :url="'http://opendata.pref.toyama.jp/dataset/covid19'"
      >
        <template v-slot:additionalDescription>
          <span>{{ $t('（注）') }}</span>
          <ul>
            <li>
              {{
                $t(
                  '検体採取日を基準とする'
                )
              }}
            </li>
            <li>
              {{ $t('2020年10月31日以前は、検査結果判明日を基準とする') }}
            </li>
            <li>
              {{
                $t(
                  '2020年2月27日には、2020年2月26日以前までの累計数を含む'
                )
              }}
            </li>
            <li>
              {{ $t('把握には一定の期間を要しており、更新日時における最新情報とは異なる場合がある') }}
            </li>
          </ul>
        </template>
      </time-stacked-bar-chart>
    </client-only>
  </v-col>
</template>

<script>
import dayjs from 'dayjs'
import duration from 'dayjs/plugin/duration'
import TimeStackedBarChart from '@/components/TimeStackedBarChart.vue'
import Data from '@/data/tested_number.json'
dayjs.extend(duration)

export default {
  components: {
    TimeStackedBarChart,
  },
  data() {
    const date = Data.date
    const inspectionsGraph = [
      Data.data['PCR検査数'],
      Data.data['抗原検査数'],
    ]
    const inspectionsItems = [
      this.$t('PCR検査数'),
      this.$t('抗原検査数')
    ]
    const inspectionsLabels = Data.data['年月日']
    const inspectionsDataLabels = [
      this.$t('PCR検査数'),
      this.$t('抗原検査数')
    ]
    const inspectionsTableLabels = [
      this.$t('PCR検査数'),
      this.$t('抗原検査数')
    ]
    return {
      date,
      inspectionsGraph,
      inspectionsItems,
      inspectionsLabels,
      inspectionsDataLabels,
      inspectionsTableLabels,
    }
  },
}
</script>
