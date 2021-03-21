<template>
  <v-col cols="12" md="6" class="DataCard">
    <client-only>
      <time-bar-chart
        :title="$t('受診・相談センターへの相談件数')"
        :title-id="'center-consultation-number'"
        :chart-id="'center-consultation-number'"
        :chart-data="contactsGraph"
        :date="date"
        :unit="$t('件.reports')"
        :url="'http://opendata.pref.toyama.jp/dataset/covid19'"
      >
        <template v-slot:additionalDescription>
          <span>{{ $t('（注）') }}</span>
          <ul>
            <li>
              {{
                $t(
                  '2020年2月27日には、2020年2月26日以前までの累計数を含む'
                )
              }}
            </li>
            <li>
              {{
                $t(
                  '2020年11月8日以前は、帰国者・接触者相談センターへの相談件数'
                )
              }}
            </li>
            <li>
              {{ $t('把握には一定の期間を要しており、更新日時における最新情報とは異なる場合がある') }}
            </li>
          </ul>
        </template>
      </time-bar-chart>
    </client-only>
  </v-col>
</template>

<script>
import TimeBarChart from '@/components/TimeBarChart.vue'
import Data from '@/data/center_consultation_number.json'
import formatGraph from '@/utils/formatGraph'

export default {
  components: {
    TimeBarChart,
  },
  data() {
    const date  = Data.date
    const contactsGraph = formatGraph(Data.data)
    return {
      contactsGraph,
      date,
    }
  },
}
</script>
