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
<br><br>
<div class="columns">
	<div class="column">
		<div class="tile is-parent">
			<article class="tile is-child box">
				<ul>
				</ul>
			</article>
		</div>
	</div>
	<div class="column">
		<div class="tile is-parent">
			<article class="tile is-child box">
				<h1 class="title">Points: {$pts}</h1>
				<h3 class="subtitle">CPS: {$clicksps}</h3>
			</article>
		</div>
	</div>
	<div class="column"></div>
</div>
