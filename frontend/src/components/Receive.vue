<!-- HTMLを記述 -->
<template>
  <div class="receive">
    <p>口座番号と入金額を入力してください。</p>
    <el-form style="margin: 0 150px;" :model="receiveForm" ref="receiveForm" :rules="rules">
      <el-form-item class="input" prop="id" label="口座番号">
        <el-input type="id" v-model="receiveForm.id" autocomplete="off"></el-input>
      </el-form-item>
      <el-form-item class="input" prop="amount" label="入金額">
        <el-input type="amount" v-model.number="receiveForm.amount" autocomplete="off"></el-input>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="submitForm('receiveForm')">入金</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'receive',
  data () {
    return {
      receiveForm: {
        id: '',
        amount: 0
      },
      rules: {
        id: [
          { required: true, message: '口座番号は必ず入力してください。' },
          { pattern: /^[0-9]{5}$/, message: '数字5桁で入力してください。' }
        ],
        amount: [
          { required: true, message: '入金額は必ず入力してください。' },
          { type: 'number', message: '正しい数値を入力してください。' }
        ]
      },
      responseMsg: '',
      randomNum: 0
    }
  },
  methods: {
    getRandom () {
      this.randomNum = this.getRandomNum()
    },
    getRandomNum () {
      const path = 'http://localhost:5000/rand'
      axios.get(path)
        .then(response => {
          this.randomNum = response.data.randomNum
        })
        .catch(error => {
          console.log(error)
        })
    },
    submitForm (formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {
          alert('submit!')
          const path = 'http://localhost:5000/receive'
          axios.post(path)
            .then(response => {
              this.responseMsg = response.data.responseMsg
            })
        } else {
          console.log('error submit!!')
          return false
        }
      })
    }
  },
  created () {
    this.getRandom()
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
