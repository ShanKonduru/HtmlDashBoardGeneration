from flask import Flask, render_template
import os

app = Flask(__name__)

print("Current Working Directory:", os.getcwd())
template_file = r"C:\\MyProjects\\HtmlDashBoardGeneration\\templates\\index.html"
# template_file = os.path.join(app.root_path, 'templates', 'index.html')

def render_page(title, header_title, header_content, header_images,
                sidebar_title, sidebar_content, sidebar_images,
                main_content, main_images,
                footer_title, footer_content, footer_images):
    
    if os.path.exists(template_file):
        print(f"The template file '{template_file}' exists.")
    else:
        print(f"The template file '{template_file}' does not exist.")

    return render_template(template_file,
                           page_title=title,
                           header_title=header_title,
                           header_content=header_content,
                           header_images=header_images,
                           sidebar_title=sidebar_title,
                           sidebar_content=sidebar_content,
                           sidebar_images=sidebar_images,
                           main_content=main_content,
                           main_images=main_images,
                           footer_title=footer_title,
                           footer_content=footer_content,
                           footer_images=footer_images)

@app.route('/')
def index():
    return render_page(
        title="Hotel Tips Dashboard",
        header_title="Bar Chart Matplot lib",
        header_content="Bar Chart Matplot lib",
        header_images=['inputImages/BarChartMatplotlib.png'],
        
        sidebar_title="Bokeh Graphs",
        sidebar_content="Bokeh Graphs",
        sidebar_images=['./inputImages/bokehbarchart.png', './inputImages/bokehlineplot.png', './inputImages/bokehscatterplot.png'],
        
        main_content="Matlib Plot Graphs",
        main_images=['./inputImages/linechartmatplotlib.png','./inputImages/matplotlibhostogram.png', './inputImages/matplotlibscatterplotwithcolors.png','./inputImages/scatterplotmatplotlib.png'],

        footer_title="Seaborn Graphs",
        footer_content="Seaborn Graphs",
        footer_images=[
            './inputImages/linechartwithcolorseaborn.png',
            './inputImages/histogramseaborn.png',
            './inputImages/seabornbarplot.png',
            './inputImages/seabornscatterplot.png',
            './inputImages/seabornscatterplotwithcolors.png',
            './inputImages/seabornwithmatplotlib.png',
            './inputImages/tipsdatasetloadpandas.png']
    )

if __name__ == '__main__':
    app.run(debug=True)
