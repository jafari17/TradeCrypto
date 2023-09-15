<template>
  <form @submit.prevent="handleSubmit">
    <label>entry date:</label>
    <input v-model="entry_date" type="date" required>
    <label>type position:</label>
    <select v-model="type_position">
      <option value="buy"> Buy </option>
      <option value="sell"> Sell </option>
    </select>
    <label>currency:</label>
    <select v-model="currency">
      <option value="BTCUSDT"> BTCUSDT </option>
      <option value="ETHUSDT"> ETHUSDT </option>
    </select>
    <label>Entry Price:</label>
    <input v-model="entry_price" type="number">
    <label>Dollar Value:</label>
    <input v-model="dollar_value" type="number">
    <label>Coin Value:   </label>
    <div class="wrapper">
    <input class="inputSpan" v-model="coin_value" type="number" step="0.00001"  disabled />
    <span  @click="handleRatio" class="material-icons x">calculate</span>
    </div>

    <label>notes:</label>
    <input v-model="notes" validate="isNotEmpty" required="false" >
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
      entry_price:0,
      dollar_value:0,
      coin_value:(this.dollar_value / this.entry_price).toFixed(5),
      notes:'  ',
    }
  },
  methods:{

    handleRatio(){

      this.coin_value = (this.dollar_value / this.entry_price).toFixed(5)

    },



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
   font-weight: 700;

 }
label {
  display: block;
  color: #bbb;
  text-transform: uppercase;
  font-size: 14px;
  letter-spacing: 1px;
  margin: 20px 0 10px 0;

}
input{
  padding: 10px;
  border: 0;
  border-bottom: 1px solid #ddd ;
  width: 100%;
  box-sizing: border-box;
  font-size: large;

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
  font-size: large;
}
select{
  padding: 10px;
  border: 0;
  border-bottom: 1px solid #ddd ;
  width: 100%;
  box-sizing: border-box;
  font-weight: 700;
  font-size: large;
}
.x {

  font-size: xx-large;
  margin-left: 0;
  padding-top: 0;
  color:blue;
  cursor: pointer;
}
.x:hover{
  color: #777;
}


.wrapper {
    position: relative;
}

.inputSpan {
    padding-left: 50px;

}

.wrapper span {
    position: absolute;
    left: 2px;
}


</style>