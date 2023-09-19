

<template>

    <div class="project" >
    <div class="actions">

      <tr>
        <th>  ---  {{ balanceSheet['BTCUSDT'] }}  --- </th>
          <br/>
        <th> Dollar Value: {{balanceSheet['BTCUSDT'].dollarValue.toFixed(2)}}</th>
          <br/>
        <th> Coin Value: {{balanceSheet['BTCUSDT'].coinValue.toFixed(2)}}</th>
          <br/>
        <th> Last Price BTCUSDT: {{last_price_coin.BTCUSDT}}</th>
          <br/>
        <th> Asset Value: {{balanceSheet['BTCUSDT'].assetValue.toFixed(2)}}</th>
          <br/>
        <th> Balance Sheet : {{balanceSheet['BTCUSDT'].balanceSheetCoin.toFixed(2)}}</th>
      </tr>
            <div class="icons">
               <span  @click="HandleRefresh" class="material-icons">refresh</span>
            </div>
    </div>
  </div>


</template>


<script >

export default {
  props: ['balanceSheet'],
  data() {
  },
}

</script>
<style >

</style>