<template>
  <div class="init">
    <h1>さぁ、口座を作ろう。</h1>
    <el-row>
      <el-button type="success" class="btn" @click="makeAccount">作る！</el-button>
    </el-row>
    <h1>{{ msg }}</h1>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'init',
  data () {
    return {
      msg: ''
    }
  },
  methods: {
    makeAccount () {
      const path = 'http://localhost:5000/init'
      axios.get(path)
        .then(response => {
          var accountId
          accountId = response.data.accountId
          this.msg = 'あなたの口座番号は【 ' + accountId + ' 】です。'
        })
        .catch(error => {
          console.log(error)
          this.msg = '作成に失敗しました。。\n時間をおいて再度トライしてみてください。'
        })
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}
.btn {
  margin: 20px;
  transform: scale(2);
}
</style>
