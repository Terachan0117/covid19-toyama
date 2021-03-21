<template>
  <v-col cols="12" md="6" class="DataCard">
    <client-only>
      <monitoring-line-chart
        :title="$t('モニタリング項目(A)')"
        title-id="monitoring-positive-rate"
        :info-titles="[$t('陽性率')]"
        chart-id="monitoring-positive-rate"
        :chart-data="graphData"
        :date="date"
        :unit="$t('%')"
      >
        <template v-slot:additionalDescription>
          <span>{{ $t('（注）') }}</span>
          <ul>
            <li>
              {{
                $t(
                  '直近1週間1日当たりの平均値'
                )
              }}
            </li>
          </ul>
        </template>
      </monitoring-line-chart>
    </client-only>
  </v-col>
</template>

<script>
import AppLink from '@/components/AppLink.vue'
import MonitroingLineChart from '@/components/MonitoringLineChart.vue'
import Data from '@/data/monitoring_status.json'
import { convertDateToISO8601Format } from '@/utils/formatDate.ts'

export default {
  components: {
    MonitroingLineChart,
    AppLink,
  },
  data() {
    const { date } = Data
    const graphData = Data.data
      .map((d) => ({
        label: convertDateToISO8601Format(d.date),
        transition: d.positive_rate,
      }))
    return {
      graphData,
      date,
    }
  },
}
</script>
