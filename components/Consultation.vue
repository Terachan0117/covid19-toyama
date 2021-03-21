<template>
  <v-col cols="12" md="6">
    <lazy-static-info
      class="Consultation"
      url="http://www.pref.toyama.jp/cms_sec/1205/kj00021473.html"
      :text="$t('自分や家族の症状に不安や心配があればまずは電話相談をどうぞ')"
      :btn-text="$t('相談の手順を見る')"
    />
  </v-col>
</template>

<style lang="scss" scoped>
.Consultation {
  padding: 18px;
  min-height: 8em;
}
</style>
