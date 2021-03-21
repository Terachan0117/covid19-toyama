<template>
  <ul :class="$style.container">
    <li :class="[$style.box]">
      <div :class="$style.content">
        <span>(1) {{ $t('入院者数') }} ({{ $t('基準: 100人未満') }})</span>
        <monitoring-items-overview-table-value-with-translatable-unit
          :value="items['(1)入院者数'].value"
          :unit="items['(1)入院者数'].unit"
        />
      </div>
    </li>
    <li :class="[$style.box]">
      <div :class="$style.content">
        <span>(2) {{ $t('重症病床稼働率') }} ({{ $t('基準: 30%未満') }})</span>
        <monitoring-items-overview-table-value-with-translatable-unit
          :value="items['(2)重症病床稼働率'].value"
          :unit="items['(2)重症病床稼働率'].unit"
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
