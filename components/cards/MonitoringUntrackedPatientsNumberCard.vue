<template>
  <v-col cols="12" md="6" class="DataCard">
    <client-only>
      <monitoring-bar-chart
        :title="$t('モニタリング項目(4)')"
        title-id="monitoring-untracked-patients-number"
        :info-titles="[$t('感染経路不明の新規陽性者数')]"
        chart-id="monitoring-untracked-patients-number"
        :chart-data="graphData"
        :date="date"
        :unit="$t('人')"
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
            <li>
              {{
                $t(
                  '人口100万人当たりの値'
                )
              }}
            </li>
          </ul>
        </template>
      </monitoring-bar-chart>
    </client-only>
  </v-col>
</template>

<script>
import AppLink from '@/components/AppLink.vue'
import MonitroingBarChart from '@/components/MonitoringBarChart.vue'
import Data from '@/data/monitoring_status.json'
import { convertDateToISO8601Format } from '@/utils/formatDate.ts'

export default {
  components: {
    MonitroingBarChart,
    AppLink,
  },
  data() {
    const { date } = Data
    const graphData = Data.data
      .map((d) => ({
        label: convertDateToISO8601Format(d.date),
        transition: d.untracked_patients_number,
      }))
    return {
      graphData,
      date,
    }
  },
}
</script>
