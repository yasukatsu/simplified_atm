<template>
  <div class="receive">
    <h3>口座番号と出金額を入力してください。</h3>
    <el-form style="margin: 0 150px;" :model="payForm" ref="payForm" :rules="rules">
      <el-form-item class="input" prop="accountId" label="口座番号">
        <el-input type="accountId" v-model="payForm.accountId" autocomplete="off"></el-input>
      </el-form-item>
      <el-form-item class="input" prop="amount" label="出金額">
        <el-input type="amount" v-model.number="payForm.amount" autocomplete="off"></el-input>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="submitForm('payForm')">入金</el-button>
      </el-form-item>
    </el-form>
    <h3>{{msg}}</h3>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'pay',
  data () {
    return {
      payForm: {
        accountId: '',
        amount: 0
      },
      rules: {
        accountId: [
          { required: true, message: '口座番号は必ず入力してください。' },
          { pattern: /^[0-9]{1,5}$/, message: '正しい値を入力してください。' }
        ],
        amount: [
          { required: true, message: '出金額は必ず入力してください。' },
          { type: 'number', message: '正しい数値を入力してください。' }
        ]
      },
      msg: ''
    }
  },
  methods: {
    submitForm (formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {
          const path = 'http://localhost:5000/pay'
          var responseMsg
          var totalAmount
          axios.post(path, {
            accountId: this.payForm.accountId,
            amount: this.payForm.amount
          })
            .then(response => {
              responseMsg = response.data.responseMsg
              totalAmount = response.data.totalAmount
              console.log(responseMsg)
              console.log(totalAmount)
            })
          console.log(responseMsg)
          // var response = await this.request()

          // if (response === null) {
          //   this.msg = '入金に失敗しました。時間をおいて再度お試しください。'
          //   return
          // }

          // var responseMsg = response.data.responseMsg
          // var totalAmount = response.data.totalAmount
          // if (responseMsg === 'ok') {
          //   this.msg = '入金に成功しました。残高は【 ' + totalAmount + '円 】です。'
          // } else {
          //   this.msg = '入金に失敗しました。口座番号をご確認の上再度お試しください。'
          // }

          setTimeout(() => {
            // ここに遅らせた後に行いたい処理を書く。関数でもOK
            console.log(responseMsg)
            if (responseMsg === 'ok') {
              this.msg = '出金に成功しました。残高は' + totalAmount + '円です。'
            } else {
              this.msg = '出金に失敗しました。口座番号をご確認の上再度お試しください。'
            }
          }, 1000)
        } else {
          return false
        }
      })
    }
    // request: async function () {
    //   const path = 'http://localhost:5000/receive'
    //   var res = null
    //   await axios.post(path, {
    //     // リクエストで送るパラメータを設定
    //     accountId: this.payForm.accountId,
    //     amount: this.payForm.amount
    //   })
    //     .then(response => {
    //       res = response
    //       // responseMsg = response.data.responseMsg
    //       // totalAmount = response.data.totalAmount
    //     })
    //     .catch(error => {
    //       console.log(error)
    //     })
    //   return res

    // }
  }
}
</script>

<style scoped>
/* .receive {
  position: absolute;
  top: 50px;
  left: 300px;
} */
</style>
