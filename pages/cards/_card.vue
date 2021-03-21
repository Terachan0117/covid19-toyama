<template>
  <component :is="cardComponent" />
</template>

<script lang="ts">
/* eslint-disable simple-import-sort/sort -- ブラウザでの表示順に合わせて各 card の component を import する */
// ---- モニタリング項目
// 検査陽性者の状況
import PatientsSummaryCard from '@/components/cards/PatientsSummaryCard.vue'
// 公表日別による陽性者数の推移
import PatientsNumberCard from'@/components/cards/PatientsNumberCard.vue'
// モニタリング項目の状況
import MonitoringSummaryCard from '@/components/cards/MonitoringSummaryCard.vue'
// モニタリング項目(1)入院者数
import MonitoringHospitalizedNumberCard from '@/components/cards/MonitoringHospitalizedNumberCard.vue'
// モニタリング項目(2)重症病床稼働率
import MonitoringSevereBedOccupancyRateCard from '@/components/cards/MonitoringSevereBedOccupancyRateCard.vue'
// モニタリング項目(3)新規陽性者数
import MonitoringPatientsNumberCard from '@/components/cards/MonitoringPatientsNumberCard.vue'
// モニタリング項目(4)感染経路不明の新規陽性者数
import MonitoringUntrackedPatientsNumberCard from '@/components/cards/MonitoringUntrackedPatientsNumberCard.vue'
// モニタリング項目(A)陽性率
import MonitoringPositiveRateCard from '@/components/cards/MonitoringPositiveRateCard.vue'
// ---- その他 参考指標
// 陽性患者の属性
import PatientsAttributeCard from '@/components/cards/PatientsAttributeCard.vue'
// 陽性者数（市町村別）
import PatientsByMunicipalitiesCard from '@/components/cards/PatientsByMunicipalitiesCard.vue'
// 検査実施件数
import TestedNumberCard from '@/components/cards/TestedNumberCard.vue'
// 新型コロナウイルス感染症に関する一般相談件数
import ConsultationNumberCard from '@/components/cards/ConsultationNumberCard.vue'
// 受診・相談センターへの相談件数
import CenterConsultationNumberCard from '@/components/cards/CenterConsultationNumberCard.vue'
/* eslint-enable simple-import-sort/sort */

import { Vue, Component } from 'nuxt-property-decorator'
import type { NuxtOptionsHead as MetaInfo } from '@nuxt/types/config/head'
import type { NuxtConfig } from '@nuxt/types'
import { getLinksLanguageAlternative } from '@/utils/i18nUtils'
import { convertDateToSimpleFormat } from '@/utils/formatDate'

@Component({
  components: {
    // ---- モニタリング項目
    PatientsSummaryCard,
    PatientsNumberCard,
    MonitoringSummaryCard,
    MonitoringHospitalizedNumberCard,
    MonitoringSevereBedOccupancyRateCard,
    MonitoringPatientsNumberCard,
    MonitoringUntrackedPatientsNumberCard,
    MonitoringPositiveRateCard,
    // ---- その他 参考指標
    PatientsAttributeCard,
    PatientsByMunicipalitiesCard,
    TestedNumberCard,
    ConsultationNumberCard,
    CenterConsultationNumberCard,
  },
})
export default class CardContainer extends Vue implements NuxtConfig {
  data() {
    let title, updatedAt, cardComponent
    switch (this.$route.params.card) {
      // NOTE: 以下，ブラウザでの表示順に合わせて条件分岐を行う
      // ---- モニタリング項目
      // 検査陽性者の状況
      case 'patients-summary':
        cardComponent = 'patients-summary-card'
        break
      // 公表日別による陽性者数の推移
      case 'patients-number':
        cardComponent = 'patients-number-card'
        break
      // モニタリング項目の状況
      case 'monitoring-summary':
        cardComponent = 'monitoring-summary-card'
        break
      // モニタリング項目(1)入院者数
      case 'hospitalized-number':
        cardComponent = 'hospitalized-number-card'
        break
      // モニタリング項目(2)重症病床稼働率
      case 'monitoring-severe-bed-occupancy-rate':
        cardComponent = 'monitoring-severe-bed-occupancy-rate-card'
        break
      // モニタリング項目(3)新規陽性者数
      case 'monitoring-patients-number':
        cardComponent = 'monitoring-patients-number-card'
        break
      // モニタリング項目(4)感染経路不明の新規陽性者数
      case 'monitoring-untracked-patients-number':
        cardComponent = 'monitoring-untracked-patients-number-card'
        break
      // モニタリング項目(A)陽性率
      case 'monitoring-positive-rate':
        cardComponent = 'monitoring-positive-rate-card'
        break
      // ---- その他 参考指標
      /*
      // 陽性患者の属性
      case 'patients-attribute':
        cardComponent = 'patients-attribute-card'
        break
      */
      // 陽性者数（市町村別）
      case 'patients-by-municipalities':
        cardComponent = 'patients-by-municipalities-card'
        break
      // 検査実施件数
      case 'tested-number':
        cardComponent = 'tested-number-card'
        break
      // 新型コロナウイルス感染症に関する一般相談件数
      case 'consultation-number':
        cardComponent = 'consultation-number-card'
        break
      // 受診・相談センターへの相談件数
      case 'center-consultation-number':
        cardComponent = 'center-consultation-number-card'
        break      
    }
    /* eslint-enable simple-import-sort/sort */
    return {
      cardComponent,
      title,
      updatedAt,
    }
  }

  head() {
    const url = 'https://stopcovid19-toyama.netlify.app/'
    const timestamp = new Date().getTime()
    const defaultTitle = `${this.$t('富山県')} ${this.$t(
      '新型コロナウイルス感染症'
    )}${this.$t('対策サイト')}`
    const ogpImage = this.$tc('ogp.og:image')

    const mInfo: MetaInfo = {
      title: `${
        (this.$data.title ?? '') !== ''
          ? this.$data.title + ' | ' + defaultTitle
          : defaultTitle
      }`,
      link: [
        ...(getLinksLanguageAlternative(
          `cards/${this.$route.params.card}`,
          this.$i18n.locales,
          this.$i18n.defaultLocale
        ) as []),
      ],
      meta: [
        {
          hid: 'og:url',
          property: 'og:url',
          content: `${url}${this.$route.path}/`,
        },
        {
          hid: 'og:title',
          property: 'og:title',
          content: `${
            (this.$data.title ?? '') !== ''
              ? this.$data.title + ' | ' + defaultTitle
              : defaultTitle
          }`,
        },
        {
          hid: 'description',
          name: 'description',
          content: `${this.$t('{date} 更新', {
            date: convertDateToSimpleFormat(this.$data.updatedAt),
          })}: ${this.$tc(
            '富山県の新型コロナウイルス感染症 (COVID-19) に関する最新情報を提供しています。'
          )}`,
        },
        {
          hid: 'og:description',
          property: 'og:description',
          content: `${this.$t('{date} 更新', {
            date: convertDateToSimpleFormat(this.$data.updatedAt),
          })}: ${this.$tc(
            '富山県の新型コロナウイルス感染症 (COVID-19) に関する最新情報を提供しています。'
          )}`,
        },
        {
          hid: 'og:image',
          property: 'og:image',
          content: `${ogpImage}`,
        },
        {
          hid: 'twitter:image',
          name: 'twitter:image',
          content: `${ogpImage}`,
        },
      ],
    }
    return mInfo
  }
}
</script>
