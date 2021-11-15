<template>
  <div id="app">
    <!-- <h1>ようこそ！でぶとれ銀行へ！</h1> -->
    <!-- <el-menu :default-active="activeIndex" mode="horizontal" router>
      <el-menu-item index="pay" :route="{ name:'pay' }">出金</el-menu-item>
      <el-menu-item index="receive" :route="{ name:'receive' }">入金</el-menu-item>
      <el-menu-item>
        <a href="https://element.eleme.io" target="_blank">Link</a>
      </el-menu-item>
    </el-menu> -->
    <h2>
      <img class="image" src="./assets/logo.png">
      でぶとれ銀行
    </h2>
    <el-row class="tac">
      <el-col :span="3">
        <el-menu default-active="activeIndex" class="el-menu-vertical-demo" router>
          <el-menu-item index="receive" :route="{ name:'receive' }" plain>
            <i class="el-icon-menu"></i>
            <span>入金</span>
          </el-menu-item>
          <el-menu-item index="pay" :route="{ name:'pay' }" plain>
            <i class="el-icon-menu"></i>
            <span>出金</span>
          </el-menu-item>
        </el-menu>
      </el-col>
    </el-row>
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
a {
  text-decoration: none;
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
