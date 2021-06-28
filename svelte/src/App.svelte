<script>
	import { pts, clicksps } from './stores.js'
	import { onMount } from 'svelte'
	
	let points;
	let cps; 
	onMount(() => {
		pts.subscribe((value) => {
			points = value
		})
		clicksps.subscribe((value) => {
			cps = value
		})
	})
	
</script>

<main>
	<h1>{points}</h1>
	<h4>{cps}</h4>
</main>