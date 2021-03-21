<template>
  <v-col cols="12" md="6" class="DataCard">
    <client-only>
      <monitoring-line-chart
        :title="$t('モニタリング項目(2)')"
        title-id="monitoring-severe-bed-occupancy-rate"
        :info-titles="[$t('重症病床稼働率')]"
        chart-id="monitoring-severe-bed-occupancy-rate"
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
        transition: d.severe_bed_occupancy_rate,
      }))
    return {
      graphData,
      date,
    }
  },
}
</script>
