let page = 0
let can_load = true

//:1 Load Data
let load_data = () => {
  const data = {
    ':method': 'load',
    page: (page + 1)
  }

  $.post('/api/', data).done((data) => {
    data = $.parseJSON(data)
    if (data.status == "error") {
      return
    }
    page += 1
    $.each(data.articles, (i, news) => {
      let date = new Date(news.publishedAt)
      let element = `
        <div class="column">
          <a class="picture" href="${news.url}">
            <img src="${news.urlToImage}" alt="${news.description}">
          </a>
          <div class="title">
            <a href="${news.url}">${news.title}</a>
          </div>
          <div class="caption">${date}</div>
        </div>`
      $('.columns').append(element)
    })
    can_load = true
  })
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
    load_data()
    $('html, body').stop().animate({scrollTop: position+15}, 1000)
  }
})
