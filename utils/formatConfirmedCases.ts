type DataType = {
  attr: '陽性者数'
      value: number
      children: [
        {
          attr: '入院'
          value: number
          children: [
            {
              attr: '軽症・中等症'
              value: number
            },
            {
              attr: '重症'
              value: number
            }
          ]
        },
        {
          attr: '宿泊療養'
          value: number
        },
        {
          attr: '死亡'
          value: number
        },
        {
          attr: '退院等'
          value: number
        }
      ]
}

type ConfirmedCasesType = {
  陽性者数: number
  入院: number
  軽症中等症: number
  重症: number
  宿泊療養: number
  死亡: number
  退院等: number
}

interface ChildData {
  attr: string
  value: number
}

type ChildDataType = {
  attr?: string
  value?: number
  children?: ChildData[]
}

function getSelectedItem(data: DataType, key: string) {
  let result: number | undefined
  const recursiveSearch = (data: ChildDataType) => {
    if (result) {
      return
    }
    if (data.attr === key) {
      result = data.value
    } else if (data.children) {
      data.children.forEach((child: ChildDataType) => {
        if (result) {
          return
        }
        recursiveSearch(child)
      })
    }
  }
  recursiveSearch(data)

  return result || 0
}

/**
 * Format for *Chart component
 *
 * @param data - Raw data
 */
export default (data: DataType) => {
  return {
    陽性者数: getSelectedItem(data, '陽性者数'),
    入院: getSelectedItem(data, '入院'),
    軽症中等症: getSelectedItem(data, '軽症・中等症'),
    重症: getSelectedItem(data, '重症'),
    宿泊療養: getSelectedItem(data, '宿泊療養'),
    死亡: getSelectedItem(data, '死亡'),
    退院等: getSelectedItem(data, '退院等'),
  } as ConfirmedCasesType
}
