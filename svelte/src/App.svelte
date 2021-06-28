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
					<li>Lorem ipsum dolor sit amet consectetur adipisicing elit. Maxime doloribus officiis, ratione suscipit consequuntur debitis provident a harum nisi dignissimos distinctio fugit dicta quasi qui! Pariatur ab hic nihil repudiandae.</li>
					<li>Deserunt necessitatibus hic nisi alias veniam ex asperiores nobis quos vitae facere iste perspiciatis eius ad eos vero, maiores labore, non voluptatum odio. Labore, officiis. Praesentium, vitae. Ipsam, iste aperiam!</li>
					<li>Soluta, iste aliquid! Placeat rem tempore iusto necessitatibus quod, fugit cupiditate omnis esse doloribus itaque at aspernatur perspiciatis odio nisi officiis ipsa animi quae? Quod unde iure mollitia pariatur reiciendis.</li>
					<li>Voluptate voluptatem laborum suscipit facere beatae cum pariatur! Placeat numquam facere in reprehenderit et ad! Quasi corrupti perferendis earum, ut quod suscipit ipsam. Ratione doloribus ex ullam error perferendis incidunt?</li>
					<li>Hic cum quod cumque, exercitationem quis eos ad. Maxime corrupti cum dignissimos qui praesentium molestiae laudantium voluptates laborum, facilis amet tempore libero ex atque nam iusto quisquam, voluptatum quibusdam. Recusandae?</li>
					<li>Pariatur velit adipisci placeat nam asperiores aperiam necessitatibus quia rerum fuga! Modi recusandae commodi ipsam repellat tenetur eaque. Odio ea, totam repellat dolore suscipit corrupti a itaque! Assumenda, aperiam consectetur.</li>
					<li>Laudantium, autem reprehenderit dolores corrupti earum modi dignissimos alias expedita aperiam consequatur ut officia quibusdam. Corrupti aliquam voluptates laudantium nostrum saepe impedit totam aperiam, dolorum aut? Laboriosam dolores ea omnis.</li>
					<li>Doloremque esse corrupti eum maiores commodi, voluptate libero debitis, cum, iusto enim distinctio aliquam iure maxime temporibus? Minus facere nobis, sapiente quod officia eaque voluptate, autem ipsa obcaecati quo perspiciatis!</li>
					<li>Nobis excepturi mollitia natus omnis doloribus suscipit officiis quibusdam delectus quas. Doloremque commodi corrupti fugit quod porro eligendi odio officia hic saepe laborum! Maiores veritatis cum iure ex praesentium voluptatibus!</li>
					<li>Reiciendis odio corporis id adipisci nemo est dolores pariatur cum quas iusto deleniti, perferendis nihil optio, omnis dolorem illo labore consectetur unde at expedita quae libero aut hic? Fugit, saepe.</li>
					<li>Possimus eligendi pariatur ducimus deserunt quo labore debitis recusandae sed, at cum ipsam quas quia, error sit cumque. Accusamus porro animi quae dolore at fugit in exercitationem, maiores blanditiis commodi?</li>
					<li>Illo in laborum, necessitatibus distinctio eligendi rerum eveniet pariatur? Quidem quaerat nulla reprehenderit praesentium aliquid asperiores fugiat ut rem, necessitatibus recusandae accusamus, iste, enim repudiandae impedit similique id. Nobis, a.</li>
					<li>Non facilis in, temporibus commodi nam impedit ad debitis. Voluptas neque natus reiciendis voluptatem earum, quia corporis suscipit, atque cupiditate quasi consequatur aperiam odio molestias reprehenderit nesciunt quisquam illo! Ex.</li>
					<li>Quia culpa est similique perspiciatis ut necessitatibus aperiam, fuga nisi blanditiis. Repellat at magni ea dignissimos nostrum quis, quo numquam quisquam voluptatum tenetur reprehenderit est soluta sit dolorem accusantium excepturi!</li>
					<li>Quod molestiae repudiandae officia culpa iure alias dolores? Inventore distinctio aliquid impedit a sequi voluptas tenetur! Iure illum, consectetur voluptates hic et deserunt, iusto dolores, cupiditate laudantium fuga necessitatibus eos!</li>
					<li>Reiciendis, consectetur velit! Sapiente recusandae sed at exercitationem, culpa quo ex placeat vero excepturi repellat cupiditate eligendi aperiam velit, quis laudantium illo. Quasi, voluptatibus earum? Corporis saepe doloribus vero obcaecati.</li>
					<li>Cumque, voluptatem ipsa eaque voluptatibus quae aut officiis distinctio aperiam sit, reprehenderit deleniti? Voluptas, totam culpa sunt aliquam voluptates, odit dignissimos, ipsam eveniet iure mollitia neque quaerat assumenda in obcaecati.</li>
					<li>Vitae eveniet eius dolorum veniam tempore itaque dolorem est obcaecati vero voluptatum magnam tempora iusto facilis eos praesentium, sapiente facere fuga atque cum nesciunt maiores! Magnam eaque ut eos! Consequatur.</li>
					<li>Itaque cupiditate fuga rerum ex labore voluptatum unde, assumenda quisquam quas architecto laborum repudiandae iure quos cum impedit aspernatur deleniti. Minus voluptatem veniam mollitia id, eveniet laborum nisi aspernatur ducimus.</li>
					<li>Iusto ullam tempore quas? Beatae illum quod modi architecto quaerat id minus eveniet corporis explicabo ad voluptatum dolorum, optio quos numquam ex aperiam nam laboriosam repellendus, adipisci nesciunt voluptatibus eaque?</li>
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
