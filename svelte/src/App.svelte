<script>
	import { onMount } from 'svelte';
	import {Button} from 'attractions'
	import BuyAuto from './BuyAuto.svelte'
	import { pts, cps } from './stores.js'
	let modalOpen = false
	

	function handleClick(){
		pts.update((n) => n+1)
	}

	onMount(() => {
		let loop = setInterval(() =>{
			pts.update(n => n+$cps)
		}, 1000)
	})
</script>

<main>
	<br><br>
	<div class="container">
		<div class="box has-text-centered">
			<h1 class="title">{$pts}</h1>
			<h1 class="subtitle">{$cps}</h1>
			<br>
		</div>
		<br><br>
		<div class="is-flex is-justify-content-center">
			<Button on:click={handleClick} outlined filled rectangle>Click for pts</Button>
		</div>
		<br>
		<div class="columns">
			<div class="column">
				<div class="box is-flex is-flex-direction-column">
					<BuyAuto name='yeet' amount=15 cost=1/>
					<BuyAuto name='yeet' amount=15 cost=1/>
					<BuyAuto name='yeet' amount=15 cost=1/>
					<BuyAuto name='yeet' amount=15 cost=1/>
					<BuyAuto name='yeet' amount=15 cost=1/>
				</div>
			</div>
			<div class="column">
				<div class="box is-fluid"></div>
			</div>
		</div>
	</div>
</main>

