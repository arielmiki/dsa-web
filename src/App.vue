<template lang="pug">
    v-app
      v-toolbar(color="secondary").white--text
        v-toolbar-title Music Genre Classifier
      router-view
      v-footer(color="primary")
        v-layout(justify-center wrap)
          v-flex(shrink)
            p.body-1 &copy; {{ new Date().getFullYear() }} — <strong>fsociety</strong>
</template>

<style lang="scss">
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
#nav {
  padding: 30px;
  a {
    font-weight: bold;
    color: #2c3e50;
    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
</style>
