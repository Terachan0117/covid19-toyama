<template>
  <v-data-table
    :headers="headers"
    :items="items"
    :items-per-page="-1"
    :hide-default-footer="true"
    :height="240"
    :fixed-header="true"
    :disable-sort="true"
    :mobile-breakpoint="0"
    class="cardTable"
    item-key="name"
  >
    <template v-slot:body="{ items }">
      <tbody>
        <tr v-for="(item, i) in items" :key="i">
          <th scope="row" class="cardTable-header">
            {{ formatDate(item[headerKey]) }}
          </th>
          <td v-for="(dataKey, j) in dataKeys" :key="j" class="text-end">
            {{ item[dataKey] }}
          </td>
        </tr>
      </tbody>
    </template>
  </v-data-table>
</template>

<script lang="ts">
import dayjs from 'dayjs'
import Vue from 'vue'
import { TranslateResult } from 'vue-i18n'
import { ThisTypedComponentOptionsWithRecordProps } from 'vue/types/options'

export type TableHeader = {
  text: TranslateResult
  value: string
  align?: string
}
export type TableItem = {
  text: string
  transition?: string
  cumulative?: string
  [key: number]: number
}
type Data = {}
type Methods = {
  formatDate: (dateString: string) => string
}
type Computed = {
  dataKeys: string[]
}
type Props = {
  headers: TableHeader[]
  items: TableItem[]
  headerKey: string
}

const options: ThisTypedComponentOptionsWithRecordProps<
  Vue,
  Data,
  Methods,
  Computed,
  Props
> = {
  props: {
    headers: {
      type: Array,
      default: () => [],
    },
    items: {
      type: Array,
      default: () => [],
    },
    headerKey: {
      type: String,
      default: 'text',
    },
  },
  computed: {
    dataKeys() {
      return this.headers
        .map((h) => h.value)
        .filter((h) => h !== this.headerKey)
    },
  },
  methods: {
    formatDate(dateString: string): string {
      const date = dayjs(new Date(dateString))
      if (date.isValid()) {
        return this.$d(date.toDate(), 'date')
      } else {
        return dateString
      }
    },
  },
}

export default Vue.extend(options)
</script>

<style lang="scss">
.cardTable {
  &.v-data-table {
    th {
      padding: 8px 10px !important;
      height: auto !important;
      border-bottom: 1px solid $gray-4 !important;
      color: $gray-2 !important;
      @include font-size(12, true);

      &.text-center {
        text-align: center;
      }
    }

    tbody {
      tr {
        color: $gray-1;
        th {
          font-weight: normal;
        }
        td {
          padding: 8px 10px !important;
          height: auto !important;
          @include font-size(12, true);

          &.text-center {
            text-align: center;
          }
        }

        &:nth-child(odd) {
          th,
          td {
            background: rgba($gray-4, 0.3);
          }
        }
      }
    }
    .v-select {
      margin-left: 10px;
    }
    &:focus {
      outline: dotted $gray-3 1px;
    }
  }
  .v-data-table__wrapper {
    box-shadow: 0 -20px 12px -12px #0003 inset;
  }
  .v-data-footer {
    @include font-size(12);
    &__pagination {
      margin-left: 0;
      margin-right: 5px;
    }
  }
  .v-data-footer__select .v-select__selections .v-select__selection--comma {
    font-size: 1.2rem;
  }
}
.v-menu__content {
  width: 80px;
  .v-list-item {
    padding: 0 8px;
  }
}
.v-list-item__title {
  font-size: 1.5rem;
}

.loading {
  visibility: hidden;
}
.FooterNote {
  margin: 0 !important;
}
.DataTable-header {
  white-space: nowrap;
}
.cardTable-header {
  white-space: nowrap !important;
}
.v-data-table .text-end {
  text-align: right;
}
</style>
