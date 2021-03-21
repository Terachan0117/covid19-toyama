<template>
  <div>
    <site-top-upper />
    <cards-monitoring />
    <cards-reference />
  </div>
</template>

<script lang="ts">
import Vue from 'vue'
import { ThisTypedComponentOptionsWithRecordProps } from 'vue/types/options'

type Data = {
  showCardsTab: boolean
}
type Methods = {
  onScroll: () => void
}
type Computed = {}
type Props = {}

const options: ThisTypedComponentOptionsWithRecordProps<
  Vue,
  Data,
  Methods,
  Computed,
  Props
> = {
  data() {
    return {
      showCardsTab: true,
    }
  },
  methods: {
    onScroll() {
      this.showCardsTab = true
    },
  },
}

export default options
</script>
