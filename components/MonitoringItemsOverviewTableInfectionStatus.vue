<template>
  <ul :class="$style.container">
    <li :class="[$style.box]">
      <div :class="$style.content">
        <span>(3) {{ $t('新規陽性者数') }} ({{ $t('基準: 2.5人未満') }})</span>
        <monitoring-items-overview-table-value-with-translatable-unit
          :value="items['(3)新規陽性者数'].value"
          :unit="items['(3)新規陽性者数'].unit"
        />
      </div>
    </li>
    <li :class="[$style.box]">
      <div :class="$style.content">
        <span>(4) {{ $t('感染経路不明の新規陽性者数') }} ({{ $t('基準: 1人未満') }})</span>
        <monitoring-items-overview-table-value-with-translatable-unit
          :value="items['(4)感染経路不明の新規陽性者数'].value"
          :unit="items['(4)感染経路不明の新規陽性者数'].unit"
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
