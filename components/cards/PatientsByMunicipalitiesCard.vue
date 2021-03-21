<template>
  <v-col cols="12" md="6" class="DataCard">
    <client-only>
      <patients-by-municipalities-table
        :title="$t('陽性者数（市町村別）')"
        :title-id="'patients-by-municipalities'"
        :chart-data="municipalitiesTable"
        :date="date"
        :info="info"
      >
        <template v-slot:additionalDescription>
          <span>{{ $t('（注）') }}</span>
          <ul>
            <li>
              {{ $t('把握には一定の期間を要しており、更新日時における最新情報とは異なる場合がある') }}
            </li>
          </ul>
        </template>
      </patients-by-municipalities-table>
    </client-only>
  </v-col>
</template>

<script>
import dayjs from 'dayjs'

import Data from '@/data/patients_by_municipalities.json'
import PatientsByMunicipalitiesTable from '~/components/PatientsByMunicipalitiesTable.vue'
import { getCommaSeparatedNumberToFixedFunction } from '~/utils/monitoringStatusValueFormatters'

const countFormatter = getCommaSeparatedNumberToFixedFunction()

export default {
  components: {
    PatientsByMunicipalitiesTable,
  },
  data() {
    const { datasets, date } = Data

    const formattedDate = dayjs(date).format('YYYY/MM/DD HH:mm')

    // 市町村ごとの陽性者数
    const municipalitiesTable = {
      headers: [],
      datasets: [],
    }

    // ヘッダーを設定
    municipalitiesTable.headers = [
      { text: this.$t('地域'), value: 'area' },
      { text: this.$t('市町村'), value: 'label' },
      { text: this.$t('陽性者数'), value: 'count', align: 'end' },
    ]

    // データを追加
    municipalitiesTable.datasets = datasets.data
      .map((d) => {
        const area = this.$t(d.area)
        const label = this.$t(d.label)
        const count = countFormatter(d.count)
        return { area, label, count }
      })

    const info = {
      sText: this.$t('{date}の累計', {
        date: this.$d(new Date(datasets.date), 'date'),
      }),
    }

    return {
      date: formattedDate,
      municipalitiesTable,
      info,
    }
  },
}
</script>
