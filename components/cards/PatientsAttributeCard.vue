<template>
  <v-col cols="12" md="6" class="DataCard">
    <client-only>
      <data-view
        :title="$t('陽性患者の属性')"
        title-id="patients-attribute"
      >
        <template v-slot:additionalDescription>
          <span>{{ $t('（注）') }}</span>
          <ul>
            <li>
              {{ $t('リンク先の関連ファイルにて公開している') }}
            </li>
            <li>
              {{ $t('把握には一定の期間を要しており、更新日時における最新情報とは異なる場合がある') }}
            </li>
          </ul>
        </template>
        <section>
          <h4>{{ $t('富山県公式ホームページ') }}</h4>
        </section>
        <div>
          <app-link
            :class="$style.button"
            to="http://www.pref.toyama.jp/cms_sec/1205/kj00021798.html"
          >
            {{ $t('県内の患者等発生状況') }}
          </app-link>
        </div>
      </data-view>
    </client-only>
  </v-col>
</template>

<script>
import AppLink from '@/components/AppLink.vue'
import DataView from '@/components/DataView.vue'

export default {
  components: {
    DataView,
    AppLink,
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
