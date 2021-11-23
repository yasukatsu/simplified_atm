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
        <el-button type="warning" @click="submitForm('payForm')">出金</el-button>
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
          var errorMsg
          axios.post(path, {
            accountId: this.payForm.accountId,
            amount: this.payForm.amount
          })
            .then(response => {
              responseMsg = response.data.responseMsg
              totalAmount = response.data.totalAmount
              errorMsg = response.data.errorMsg
            })

          // レスポンス待機時間を設定
          setTimeout(() => {
            if (responseMsg === 'ok') {
              this.msg = '出金に成功しました。残高は' + totalAmount + '円です。'
            } else {
              this.msg = '出金に失敗しました。' + errorMsg
            }
          }, 500)
        } else {
          return false
        }
      })
    }
  }
}
</script>
