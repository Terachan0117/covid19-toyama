<template>
  <v-col cols="12" md="6" class="DataCard">
    <client-only>
      <time-bar-chart
        :title="$t('公表日別による陽性者数の推移')"
        :title-id="'patients-number'"
        :chart-id="'patients-number'"
        :chart-data="patientsGraph"
        :date="date"
        :unit="$t('人')"
        :by-date="true"
      >
        <template v-slot:additionalDescription>
          <span>{{ $t('（注）') }}</span>
          <ul>
            <li>
              {{ $t('感染者の発生が公表された日を基準とする') }}
            </li>
          </ul>
        </template>
      </time-bar-chart>
    </client-only>
  </v-col>
</template>

<script>
import AppLink from '@/components/AppLink.vue'
import TimeBarChart from '@/components/TimeBarChart.vue'
import Data from '@/data/patients_number.json'
import formatGraph from '@/utils/formatGraph'

export default {
  components: {
    TimeBarChart,
    AppLink,
  },
  data() {
    // 感染者数グラフ
    const patientsGraph = formatGraph(Data.data)
    const date = Data.date

    return {
      patientsGraph,
      date,
    }
  },
}
</script>
