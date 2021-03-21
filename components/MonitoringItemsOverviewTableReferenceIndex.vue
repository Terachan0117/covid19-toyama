<template>
  <ul :class="$style.container">
    <li :class="[$style.box]">
      <div :class="$style.content">
        <span>(A) {{ $t('陽性率') }} ({{ $t('基準: 7%未満') }})</span>
        <monitoring-items-overview-table-value-with-translatable-unit
          :value="items['(A)陽性率'].value"
          :unit="items['(A)陽性率'].unit"
        />
      </div>
    </li>
    <li :class="[$style.box]">
      <div :class="$style.content">
        <span>(B) {{ $t('先週対比') }} ({{ $t('基準: 1以下') }})</span>
        <monitoring-items-overview-table-value-with-translatable-unit
          :value="items['(B)先週対比'].value"
          :unit="items['(B)先週対比'].unit"
        />
      </div>
    </li>
  </ul>
</template>

<script lang="ts">
import Vue, { PropType } from 'vue'

import MonitoringItemsOverviewTableValueWithTranslatableUnit from '@/components/MonitoringItemsOverviewTableValueWithTranslatableUnit.vue'
import { MonitoringItems } from '@/utils/formatMonitoringItems'

export default Vue.extend({
  components: {
    MonitoringItemsOverviewTableValueWithTranslatableUnit,
  },
  props: {
    items: {
      type: Object as PropType<MonitoringItems>,
      required: true,
    },
  },
})
</script>

<style lang="scss" module>
@import '@/assets/monitoringItemsTableCommon.scss';
</style>
