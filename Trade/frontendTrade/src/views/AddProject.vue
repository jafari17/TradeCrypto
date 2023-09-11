<template>
  <form @submit.prevent="handleSubmit">
    <label>entry date:</label>
    <input v-model="entry_date" type="date" required>
    <label>type position:</label>
    <input v-model="type_position" type="checkbox">
    <label>currency:</label>
    <input v-model="currency">
    <label>entry_price:</label>
    <input v-model="entry_price">
    <label>dollar_value:</label>
    <input v-model="dollar_value">
    <label>coin_value:</label>
    <input v-model="coin_value">
    <label>notes:</label>
    <input v-model="notes" >
    <button> Add </button>
  </form>

</template>

<script >
import axios from "axios";

export default {
  data(){
    return{
      entry_date: '',
      type_position: false,
      currency:'',
      entry_price:'',
      dollar_value:'',
      coin_value:'',
      notes:'',
    }
  },
  methods:{
    handleSubmit(){
      let project = {
          entry_date: this.entry_date,
          type_position: this.type_position,
          currency: this.currency,
          entry_price: this.entry_price,
          dollar_value: this.dollar_value,
          coin_value: this.coin_value,
          notes: this.notes,
      }
      console.log(project)

      axios
          .post('http://127.0.0.1:8000//portfolio/api/', project)
          .then(() => {
            this.$router.push('/')
          } )
          .catch(err => console.log(err.message))

    }

  },

}

</script>



<style >
 form{
   background: white;
   padding: 20px;
   border-radius: 10px;
 }
label {
  display: block;
  color: #bbb;
  text-transform: uppercase;
  font-size: 14px;
  font-weight: bold;
  letter-spacing: 1px;
  margin: 20px 0 10px 0;
}
input{
  padding: 10px;
  border: 0;
  border-bottom: 1px solid #ddd ;
  width: 100%;
  box-sizing: border-box;
}
textarea{
  border: 1px solid #ddd;
  padding: 10px;
  width: 100%;
  box-sizing: border-box;
  height: 100px;
}
form button{
  display: block;
  margin: 20px auto 0;
  background: green;
  color: white;
  padding: 10px;
  border: 0;
  border-radius: 6px;
  font-size: 16px;
}
</style>