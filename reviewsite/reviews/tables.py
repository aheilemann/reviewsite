import django_tables2 as tables

from .models import Review


class NumberColumn(tables.Column):
    def render(self, value):
        return '{:0.2f}'.format(value)


class ReviewTable(tables.Table):

    class Meta:
        model = Review
        attrs = {'class': 'table table-sm'}
        template_name = "django_tables2/bootstrap4.html"

        fields = [
            'vote',
            'title',
            'category',
            'modified',
            'votes.count',
            'hotscore',
        ]
        order_by = '-hotscore'

    VOTETEMPLATE = '''
    <script>
        function onArrowClick(){
            $.ajax({
                url: 'your_url_for_upvote_above',
                success: function(data) {
                    if (data.success) {
                        // display success message
                        // Mark button as voted, such as orange up arrow in reddit
                        // increase count such as;
                        $("#vote-count").html(data.votes);
                    } else {
                        // display error due to something in function above
                    }
                },
                error: function() {
                    // display error due to ajax request
                }
            });
        }
    </script>
    <a class="btn btn-success btn-sm" href="{% url "reviews:list" %}">UP</a>
    <a class="btn btn-danger btn-sm" href="#">DOWN</a>
    '''
    vote = tables.TemplateColumn(VOTETEMPLATE)

    title = tables.Column(linkify=True)
    category = tables.Column(linkify=True, attrs={"th": {"width": 150}})
    modified = tables.DateColumn(attrs={"th": {"width": 150}})
    hotscore = NumberColumn()
