let page = 0
let can_load = true

//:1 Load Data
const load_data = (position) => {
  const request = {
    url: '/api/',
    type: 'POST',
    data: {
      ':method': 'load',
      page: page + 1
    }
  }
  $.ajax(request).done(response => {
    const result = $.parseJSON(response)
    //:2 append news on news feed
    $.each(result.articles, (i, news) => {
      const date = new Date(news.publishedAt)
      const item = `
        <div class="column">
          <a class="picture" href="${news.url}">
            <img src="${news.urlToImage}" alt="${news.description}">
          </a>
          <div class="title">
            <a href="${news.url}">${news.title}</a>
          </div>
          <div class="caption">${date}</div>
        </div>`
      $('#news-feed').append(item)
    })
    // endfold2
    page += 1
    $('html, body').stop().animate({scrollTop: position+15}, 1000)
  }).fail((error) => {
    if (error.status == 426)
      console.log('Upgrade required for NEWS API')
    else
      console.log('Bad request')
  })
  setTimeout(() => can_load = true, 500)
}
// endfold

load_data()

$(window).scroll(() => {
  const position = $(window).scrollTop() + $(window).height()
  if (position+100 < $(document).height()) {
    return false
  }
  if (can_load) {
    can_load = false
    load_data(position)
  }
})
