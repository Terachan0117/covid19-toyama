<template>
  <span :class="$style.linkButton">
    <app-link
      :class="$style.textLink"
      to="https://www.pref.toyama.jp/120507/kurashi/seikatsu/seikatsueisei/toyamaalert0414.html"
    >
      <antenna-icon aria-hidden="true" :class="$style.svgIcon" />
      <span :class="$style.text">
        {{ $t('富山アラート発出中') }}
      </span>
    </app-link>
  </span>
</template>

<script lang="ts">
import Vue from 'vue'

import AppLink from '@/components/AppLink.vue'
import AntennaIcon from '@/static/antenna.svg'

export default Vue.extend({
  components: {
    AppLink,
    AntennaIcon,
  },
})
</script>

<style lang="scss" module>
.linkButton {
  background-color: $alert;
  border: 2px solid $alert;
  color: $white;
  border-radius: 3em;
  padding: 4px 8px;
  margin-right: 8px;
  display: inline-flex;
  @include font-size(14);

  .svgIcon path {
    fill: $white;
  }

  &:hover {
    background-color: $white;
    .svgIcon path {
      fill: $alert;
    }
  }

  .textLink {
    display: flex;
    align-items: center;
    color: $white !important;
    text-decoration: none;
    margin: -10px;
    padding: 10px;
    i {
      color: inherit;
    }
    &:hover {
      color: $alert !important;
    }
  }

  .text {
    margin: 0 4px;
  }

  @include lessThan($medium) {
    margin: 8px 0;
  }
}
</style>
