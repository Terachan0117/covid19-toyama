<template>
  <v-col cols="12" md="6" class="DataCard">
    <client-only>
      <data-view
        :title="$t('検査陽性者の状況')"
        :title-id="'patients-summary'"
        :date="date"
      >
        <template v-slot:additionalDescription>
          <span>{{ $t('（注）') }}</span>
          <ul>
            <li>
              {{
                $t(
                  '「重症」には、集中治療室(ICU)等での管理又は人工呼吸器管理が必要な患者を計上'
                )
              }}
            </li>
            <li>
              {{
                $t(
                  '把握には一定の期間を要しており、確認次第数値を更新している'
                )
              }}
            </li>
          </ul>
        </template>
        <confirmed-cases-details-table
          :aria-label="$t('検査陽性者の状況')"
          v-bind="confirmedCases"
        />
        <!--
        <div>
          <app-link
            :class="$style.button"
            to="https://www.fukushihoken.metro.tokyo.lg.jp/iryo/kansen/shibou.html"
          >
            {{ $t('死亡日別による死亡者数の推移はこちら') }}
          </app-link>
        </div>
        -->
      </data-view>
    </client-only>
  </v-col>
</template>

<script>
import dayjs from 'dayjs'

import AppLink from '@/components/AppLink.vue'
import ConfirmedCasesDetailsTable from '@/components/ConfirmedCasesDetailsTable.vue'
import DataView from '@/components/DataView.vue'
import Data from '@/data/patients_summary.json'
import formatConfirmedCases from '@/utils/formatConfirmedCases'

const options = {
  components: {
    DataView,
    ConfirmedCasesDetailsTable,
    AppLink,
  },
  data() {
    const mainSummary = Data
    // 検査陽性者の状況
    const confirmedCases = formatConfirmedCases(mainSummary)

    const date = dayjs(mainSummary.date).format('YYYY/MM/DD HH:mm')

    return {
      confirmedCases,
      date,
    }
  },
}

export default options
</script>

<style lang="scss" module>
.button {
  margin: 20px 0 0;
  color: $green-1 !important;
  &:hover {
    color: $white !important;
  }

  @include button-text('sm');
}
</style>
