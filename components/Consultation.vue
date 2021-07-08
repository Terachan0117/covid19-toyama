<template>
  <v-col cols="12">
    <lazy-static-info
      class="Consultation"
      url="https://www.pref.toyama.jp/120507/kurashi/soudanshisetsu/madoguchi/kenkouiryou/kj00021473.html"
      :text="$t('自分や家族の症状に不安や心配があればまずは電話相談をどうぞ')"
      :btn-text="$t('相談の手順を見る')"
    />
  </v-col>
</template>

<style lang="scss" scoped>
.Consultation {
  padding: 18px;
}
</style>
