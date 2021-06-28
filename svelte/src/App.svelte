<script>
	import { pts, clicksps } from './stores.js'
	import { onMount } from 'svelte'
	import  BuyAuto  from './BuyAuto.svelte'
	
	
	let points;
	let cps; 
	onMount(() => {
		pts.subscribe((value) => {
			points = value
		})
		clicksps.subscribe((value) => {
			cps = value
		})
		let loop = setInterval(() => {
			pts.set($pts + $clicksps)
		}, 1000)
	})
	
	function buttonClick(){
		pts.set($pts + 1)
	}
</script>

<main>
	<h1>{points}</h1>
	<h4>{cps}</h4>
	<button on:click={buttonClick}>Click for points</button>
	<BuyAuto name='yeet' price='15' amount='1'/>
</main>