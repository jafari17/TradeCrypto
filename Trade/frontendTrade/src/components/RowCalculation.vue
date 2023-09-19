<template>

<div v-for="(value, key1) in balanceSheets" >

  <div class="project" >
    <div class="actions">
      <tr>
        <th>  ---  {{ key1 }}  --- </th>
          <br/>
        <th> Dollar Value: {{value.dollarValue.toFixed(2)}}</th>
          <br/>
        <th> Coin Value: {{value.coinValue.toFixed(2)}}</th>
          <br/>
        <th> Last Price {{ key1 }}: {{last_price_coin[key1] }}</th>
          <br/>
        <th> Asset Value: {{value.assetValue.toFixed(2)}}</th>
          <br/>
        <th> Balance Sheet : {{value.balanceSheetCoin.toFixed(2)}}</th>
      </tr>
            <div class="icons">
               <span  @click="HandleRefresh" class="material-icons">refresh</span>
            </div>
    </div>
  </div>
</div>


</template>

<script >
import axios from "axios";
import SingleProject from "@/components/SingleProject.vue";
import BalanceSheet from "@/components/BalanceSheet.vue";

export default {
  components: {BalanceSheet, SingleProject},
  props: ['projects'],
  data(){
    return{
      last_price_coin:0.0,
      balanceSheets: {},
    }
  },
  mounted() {
    this.HandleRefresh()
  },
  methods: {
    HandleRefresh() {
      axios
          .get("http://127.0.0.1:8000//exchange/lastPriceApi")
          .then(response => {
            this.last_price_coin = response.data
            console.log(this.last_price_coin)
            console.log(this.last_price_coin)
            console.log(this.last_price_coin)
            console.log(this.last_price_coin)
            this.calculateBalanceSheet()
          })
    },

    calculateBalanceSheet() {
    const balanceSheet = {};

    for (const project of this.projects) {
      const currency = project.currency;

      if (!balanceSheet[currency]) {
        balanceSheet[currency] = {};
        balanceSheet[currency].dollarValue = 0
        balanceSheet[currency].coinValue = 0
      }
      if (project.type_position === "sell") {
        balanceSheet[currency].dollarValue -= parseFloat(project.dollar_value);
        balanceSheet[currency].coinValue -= parseFloat(project.coin_value);
      }
      else {
        balanceSheet[currency].dollarValue += parseFloat(project.dollar_value);
        balanceSheet[currency].coinValue += parseFloat(project.coin_value);
      }
      console.log(currency)
      balanceSheet[currency].assetValue = 0
      balanceSheet[currency].balanceSheetCoin = 0

      balanceSheet[currency].assetValue = balanceSheet[currency].coinValue * this.last_price_coin[currency];
      balanceSheet[currency].balanceSheetCoin = balanceSheet[currency].assetValue - balanceSheet[currency].dollarValue;
    }

    this.balanceSheets= balanceSheet;

    //         test log

    for (let bs in balanceSheet){
      console.log(bs)
      for (let bx in balanceSheet[bs]){
      console.log(bx)
      console.log(balanceSheet[bs][bx])
      }
    }

    console.log(balanceSheet['BTCUSDT'].dollarValue)
    console.log(balanceSheet['BTCUSDT'].coinValue)
    console.log(balanceSheet['BTCUSDT'].assetValue)
    console.log(balanceSheet['BTCUSDT'].balanceSheetCoin)

    console.log(balanceSheet['ETHUSDT'].dollarValue)
    console.log(balanceSheet['ETHUSDT'].coinValue)
    console.log(balanceSheet['ETHUSDT'].assetValue)
    console.log(balanceSheet['ETHUSDT'].balanceSheetCoin)

     }
  }
}
</script>

<style scoped >
td, th {
  //border: 1px solid #dddddd;
  text-align: left;
  width: 310px;
}
</style>
