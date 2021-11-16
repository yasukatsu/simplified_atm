<template>
  <div id="app">
    <h2>
      <img class="image" src="./assets/logo.png">
      でぶとれ銀行
    </h2>
      <el-menu default-active="activeIndex" mode="horizontal" router>
        <el-menu-item index="init" :route="{ name:'init' }" plain>
          <i class="el-icon-menu"></i>
          <span>口座開設</span>
        </el-menu-item>
        <el-menu-item index="receive" :route="{ name:'receive' }" plain>
          <i class="el-icon-menu"></i>
          <span>入金</span>
        </el-menu-item>
        <el-menu-item index="pay" :route="{ name:'pay' }" plain>
          <i class="el-icon-menu"></i>
          <span>出金</span>
        </el-menu-item>
      </el-menu>
    <router-view />
  </div>
</template>

<script>
export default {
  name: 'app',
  data () {
    return {
      activeIndex: this.$route.name
    }
  }
}
</script>

<style scoped>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  text-align: center;
  color: #2c3e50;
}
h2 {
  display: flex;
  align-items: center;
}
h2 .image {
  width: 5%;
  height: auto;
}
</style>
