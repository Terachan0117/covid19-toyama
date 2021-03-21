<template>
  <div>
    <page-header class="mt-6 mb-3">
      {{ $t('モニタリング項目') }}
    </page-header>
    <v-row class="DataBlock">
      <monitoring-summary-card />
      <monitoring-hospitalized-number-card />
      <monitoring-severe-bed-occupancy-rate-card />
      <monitoring-patients-number-card />
      <monitoring-untracked-patients-number-card />
      <monitoring-positive-rate-card />
    </v-row>
  </div>
</template>

<script lang="ts">
/* eslint-disable simple-import-sort/sort -- ブラウザでの表示順に合わせて各 card の component を import する */
import Vue from 'vue'
const PageHeader = () => import('@/components/PageHeader.vue')
// モニタリング項目の状況
const MonitoringSummaryCard = () => import('@/components/cards/MonitoringSummaryCard.vue')
// モニタリング項目(1)入院者数
const MonitoringHospitalizedNumberCard = () => import('@/components/cards/MonitoringHospitalizedNumberCard.vue')
// モニタリング項目(2)重症病床稼働率
const MonitoringSevereBedOccupancyRateCard = () => import('@/components/cards/MonitoringSevereBedOccupancyRateCard.vue')
// モニタリング項目(3)新規陽性者数
const MonitoringPatientsNumberCard = () => import('@/components/cards/MonitoringPatientsNumberCard.vue')
// モニタリング項目(4)感染経路不明の新規陽性者数
const MonitoringUntrackedPatientsNumberCard = () => import('@/components/cards/MonitoringUntrackedPatientsNumberCard.vue')
// モニタリング項目(A)陽性率
const MonitoringPositiveRateCard = () => import('@/components/cards/MonitoringPositiveRateCard.vue')
/* eslint-enable simple-import-sort/sort */

export default Vue.extend({
  components: {
    PageHeader,
    MonitoringSummaryCard,
    MonitoringHospitalizedNumberCard,
    MonitoringSevereBedOccupancyRateCard,
    MonitoringPatientsNumberCard,
    MonitoringUntrackedPatientsNumberCard,
    MonitoringPositiveRateCard,
  },
})
</script>

<style lang="scss" scoped>
.DataBlock {
  .DataCard {
    margin: 8px 0;
  }
}
</style>