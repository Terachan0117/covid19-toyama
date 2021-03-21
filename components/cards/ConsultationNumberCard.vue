<template>
  <v-col cols="12" md="6" class="DataCard">
    <client-only>
      <time-bar-chart
        :title="$t('新型コロナウイルス感染症に関する一般相談件数')"
        :title-id="'consultation-number'"
        :chart-id="'consultation-number'"
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
import Data from '@/data/consultation_number.json'
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
