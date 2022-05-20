document.addEventListener("DOMContentLoaded", () => {
	const articleLinks = document.querySelector(".article_links");
	console.log(articleLinks);

	function createCardRow(title, desc, imgLink, playerName) {
		var img = document.createElement("img");
		img.src = imgLink;
		img.className = "card-img-bottom";
		var row = document.createElement("div");
		row.className = "row";
		var col = document.createElement("div");
		col.className = "col my-4";
		var card = document.createElement("div");
		card.className = "card";
		card.style = "width:40rem";
		var cardBody = document.createElement("div");
		cardBody.className = "card-body";
		var row_imbed = document.createElement("div");
		row_imbed.className = "row";
		var col_imbed = document.createElement("div");
		col_imbed.className = "col col-8 title";
		var cardTitle = document.createElement("h5");
		cardTitle.className = "card-title";
		cardTitle.innerHTML = `${title}`;
		var col_imbed2 = document.createElement("div");
		col_imbed2.className = "col topic";
		var topic = document.createElement("p");
		topic.className = "small ";
		topic.innerHTML = `${playerName}`;
		var cardBody2 = document.createElement("div");
		cardBody2.className = "card-body";
		var description = document.createElement("p");
		description.className = "card-text";
		description.innerHTML = `${desc}`;

		row_imbed.appendChild(col_imbed);
		col_imbed.append(cardTitle);
		col_imbed2.appendChild(topic);
		row_imbed.appendChild(col_imbed2);
		cardBody.appendChild(row_imbed);
		card.appendChild(cardBody);
		card.appendChild(img);

		cardBody2.appendChild(description);
		card.appendChild(cardBody2);

		var url = document.createElement("a");
		url.appendChild(card);
		url.href = "https://www.google.com";

		col.appendChild(url);
		row.appendChild(col);

		return row;
	}

	function loadLinks(n = 10) {
		for (i = 0; i < n; i++) {
			var row = createCardRow(
				"Title",
				"Description",
				"https://www.mercurynews.com/wp-content/uploads/2016/08/20110104__stanfbcluck5-2.jpg?w=792&h=576",
				"Player"
			);
			articleLinks.appendChild(row);
		}
	}

	loadLinks();
	window.addEventListener("touchmove", () => {
		if (
			window.scrollY + window.innerHeight >=
			document.documentElement.scrollHeight - 10
		) {
			loadLinks();
		}
	});
	window.addEventListener("scroll", () => {
		if (
			window.scrollY + window.innerHeight >=
			document.documentElement.scrollHeight - 10
		) {
			loadLinks();
		}
	});
});
