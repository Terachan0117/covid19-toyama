// monitoring_items.json の型チェック用

import { getCommaSeparatedNumberToFixedFunction } from '@/utils/monitoringStatusValueFormatters'

type DataKey =
  | '日付'
  | '(1)入院者数'
  | '(2)重症病床稼働率'
  | '(3)新規陽性者数'
  | '(4)感染経路不明の新規陽性者数'
  | '(A)陽性率'
  | '(B)先週対比'

type DataCommentKey = '総括コメント-感染状況' | '総括コメント-医療提供体制'

type RawData = {
  '日付': string
  '(1)入院者数': number
  '(2)重症病床稼働率': number
  '(3)新規陽性者数': number
  '(4)感染経路不明の新規陽性者数': number
  '(A)陽性率': number
  '(B)先週対比': number
}

interface Comment {
  level: number
  display: {
    '@ja': string
    '@en': string
  }
}

type RawDataComment = {
  '総括コメント-感染状況': Comment
  '総括コメント-医療提供体制': Comment
}

// -----------------------------------------
// フォーマット済み モニタリング指標データ用

export type MonitoringItems = Record<DataKey, MonitoringItemValue>

interface MonitoringItemValue {
  value: string
  unit: Unit | null // 元データに無いので独自に追加, 単位がない場合は null
}

export type Unit = {
  text: string // *********** もとの日本語のテキスト
  translatable: boolean // ** 翻訳が必要かどうか
}

/**
 * monitoring_items_json のデータを整形
 *
 * @param data - Raw data
 */
export const formatMonitoringItems = (rawDataObj: RawData): MonitoringItems => {
  const unitPerson: Unit = { text: '人', translatable: true }
  const unitReports: Unit = {
    text: '件.reports',
    translatable: true,
  }
  const unitPercentage: Unit = { text: '％', translatable: false }
  const unitNone: Unit = { text: '　', translatable: false }

  const toInteger = getCommaSeparatedNumberToFixedFunction(0)
  const toNumberIn10thPlace = getCommaSeparatedNumberToFixedFunction(1)

  return {
    '日付': {
      value: rawDataObj['日付'],
      unit: unitNone,
    },
    '(1)入院者数': {
      value: toNumberIn10thPlace(rawDataObj['(1)入院者数']),
      unit: unitPerson,
    },
    '(2)重症病床稼働率': {
      value: toNumberIn10thPlace(rawDataObj['(2)重症病床稼働率']),
      unit: unitPercentage,
    },
    '(3)新規陽性者数': {
      value: toNumberIn10thPlace(rawDataObj['(3)新規陽性者数']),
      unit: unitPerson,
    },
    '(4)感染経路不明の新規陽性者数': {
      value: toNumberIn10thPlace(rawDataObj['(4)感染経路不明の新規陽性者数']),
      unit: unitPerson,
    },
    '(A)陽性率': {
      value: toNumberIn10thPlace(rawDataObj['(A)陽性率']),
      unit: unitPercentage,
    },
    '(B)先週対比': {
      value: toNumberIn10thPlace(rawDataObj['(B)先週対比']),
      unit: unitNone,
    },
  }
}

export type MonitoringCommentItems = Record<DataCommentKey, MonitoringComment>

export type MonitoringComment = {
  level: number
  display: {
    '@ja': string
    '@en': string
  }
}

/**
 * monitoring_items_json から総括コメントのみ抜き出し
 *
 * @param data - Raw data
 */
export const formatMonitoringComment = (
  rawDataObj: RawDataComment
): MonitoringCommentItems => {
  return {
    '総括コメント-感染状況': {
      level: rawDataObj['総括コメント-感染状況'].level,
      display: {
        '@ja': rawDataObj['総括コメント-感染状況'].display['@ja'],
        '@en': rawDataObj['総括コメント-感染状況'].display['@en'],
      },
    },
    '総括コメント-医療提供体制': {
      level: rawDataObj['総括コメント-医療提供体制'].level,
      display: {
        '@ja': rawDataObj['総括コメント-医療提供体制'].display['@ja'],
        '@en': rawDataObj['総括コメント-医療提供体制'].display['@en'],
      },
    },
  }
}
