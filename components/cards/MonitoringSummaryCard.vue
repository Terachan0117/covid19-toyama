<template>
  <v-col cols="12" md="6" class="DataCard">
    <client-only>
      <data-view
        :title="$t('モニタリング項目の状況')"
        title-id="monitoring-summary"
        :date="monitoringItemsData.date"
      >
        <template v-slot:additionalDescription>
          <span>{{ $t('（注）') }}</span>
          <ul>
            <li>
              {{ $t('(1)～(4)および(A)は直近1週間1日当たりの平均値') }}
            </li>
            <li>
              {{ $t('(3)および(4)は人口100万人当たりの値') }}
            </li>
          </ul>
        </template>
        <section>
          <h4>{{ $t('医療提供体制') }}</h4>
          <monitoring-items-overview-table-medical-system
            :aria-label="$t('医療提供体制')"
            :items="monitoringItems"
          />
        </section>
        <section>
          <h4>{{ $t('感染状況') }}</h4>
          <monitoring-items-overview-table-infection-status
            :aria-label="$t('感染状況')"
            :items="monitoringItems"
          />
        </section>
        <section>
          <h4>{{ $t('参考指標') }}</h4>
          <monitoring-items-overview-table-reference-index
            :aria-label="$t('参考指標')"
            :items="monitoringItems"
          />
        </section>
        <div>
          <app-link
            :class="$style.button"
            to="http://www.pref.toyama.jp/cms_sec/1205/kj00022038.html"
          >
            {{ $t('感染拡大防止措置の強化・緩和について') }}
          </app-link>
        </div>
    <template v-slot:dataSetPanel>
      <data-view-data-set-panel
        :s-text="$t('{date} の数値', {
            date: $d(new Date(monitoringItemsData.data['日付']), 'date'),
          })"
      />
    </template>
      </data-view>
    </client-only>
  </v-col>
</template>

<script>
import dayjs from 'dayjs'
import AppLink from '@/components/AppLink.vue'
import DataView from '@/components/DataView.vue'
import DataViewDataSetPanel from '@/components/DataViewDataSetPanel.vue'
import MonitoringItemsOverviewTableMedicalSystem from '@/components/MonitoringItemsOverviewTableMedicalSystem.vue'
import MonitoringItemsOverviewTableInfectionStatus from '@/components/MonitoringItemsOverviewTableInfectionStatus.vue'
import MonitoringItemsOverviewTableReferenceIndex from '@/components/MonitoringItemsOverviewTableReferenceIndex.vue'
import monitoringItemsData from '@/data/monitoring_summary.json'
import { formatMonitoringItems } from '@/utils/formatMonitoringItems'

export default {
  components: {
    DataView,
    MonitoringItemsOverviewTableMedicalSystem,
    MonitoringItemsOverviewTableInfectionStatus,
    MonitoringItemsOverviewTableReferenceIndex,
    AppLink,
  },
  data() {
    const monitoringItems = formatMonitoringItems(monitoringItemsData.data)
    return {
      monitoringItemsData,
      monitoringItems,
    }
  },
}
</script>

<style lang="scss" module>
section {
  margin: 0 0 20px;

  /* h タグが連続するため DataView-Content の margin を少し打ち消す */
  &:first-child {
    margin-top: -10px;
  }

  h4 {
    margin: 5px 0 10px;
    font-weight: normal;
    @include font-size(16);
  }
}

.button {
  color: $green-1 !important;
  &:hover {
    color: $white !important;
  }

  @include button-text('sm');
}

dfn {
  font-style: normal;
  font-weight: 600;
}
</style>
