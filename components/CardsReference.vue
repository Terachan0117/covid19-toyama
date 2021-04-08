<template>
  <div>
    <page-header class="mt-6 mb-3">
      {{ $t('その他 参考指標') }}
    </page-header>
    <v-row class="DataBlock">
      <patients-attribute-card />
      <patients-by-municipalities-card />
      <tested-number-card />
      <consultation-number-card />
      <center-consultation-number-card />
    </v-row>
  </div>
</template>

<script lang="ts">
/* eslint-disable simple-import-sort/sort -- ブラウザでの表示順に合わせて各 card の component を import する */
import Vue from 'vue'
const PageHeader = () => import('@/components/PageHeader.vue')
// 陽性患者の属性
const PatientsAttributeCard = () => import('@/components/cards/PatientsAttributeCard.vue')
// 陽性者数（市町村別）
const PatientsByMunicipalitiesCard = () => import('@/components/cards/PatientsByMunicipalitiesCard.vue')
// 検査実施件数
const TestedNumberCard = () => import('@/components/cards/TestedNumberCard.vue')
// 新型コロナウイルス感染症に関する一般相談件数
const ConsultationNumberCard = () => import('@/components/cards/ConsultationNumberCard.vue')
// 受診・相談センターへの相談件数
const CenterConsultationNumberCard = () => import('@/components/cards/CenterConsultationNumberCard.vue')
/* eslint-enable simple-import-sort/sort */

export default Vue.extend({
  components: {
    PageHeader,
    PatientsAttributeCard,
    PatientsByMunicipalitiesCard,
    TestedNumberCard,
    ConsultationNumberCard,
    CenterConsultationNumberCard,
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