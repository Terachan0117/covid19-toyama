import { Middleware } from '@nuxt/types'

const redirect: Middleware = ({ route, redirect }) => {
  if (route.path.includes('flow')) {
    redirect(
      'http://www.pref.toyama.jp/cms_sec/1205/kj00021473.html'
    )
  }
}

export default redirect
