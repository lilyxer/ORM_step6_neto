<h2><strong>Задание 1</strong></h2>
<p>Составить модели классов SQLAlchemy по схеме:<br>
<img src="https://raw.githubusercontent.com/netology-code/py-homeworks-db/video/06-orm/readme/book_publishers_scheme.png" alt="" class="src-features-lms-lesson-hooks-useImageViewer--image--BJRv5"></p>
<p>Интуитивно необходимо выбрать подходящие типы и связи полей.</p>
<hr>
<h2><strong>Задание 2</strong></h2>
<p>Используя SQLAlchemy, составить запрос выборки магазинов, продающих целевого издателя.</p>
<p>Напишите Python скрипт, который:</p>
<ul>
<li>Подключается к БД любого типа на ваш выбор (например, к PostgreSQL).</li>
<li>Импортирует необходимые модели данных.</li>
<li>Выводит название магазинов (shop), в которых представлены книги конкретного издателя, получая имя или идентификатор издателя (publisher), через <code>input(</code>).</li>
</ul>
<hr>
<h2>**Задание 3 (необязательное)</h2>
<p>Заполните БД тестовыми данными.</p>
<p>Тестовые данные берутся из папки fixtures. Пример содержания в <a href="https://github.com/netology-code/py-homeworks-db/tree/video/06-orm/fixtures" target="_blank">JSON файле</a>.</p>
<p>Возможная реализация: прочитать json-файл, создать соотведствующие экземляры моделей и сохранить в БД.</p>
<p>Пример реализации, но сначала попытайтесь самостоятельно ;)</p>
<pre class="hljs language-"><span class="node_modules-@netology-shared-src-reallyShared-components-Markdown--lineNumber--WYPo_"><span>1</span><span>2</span><span>3</span><span>4</span><span>5</span><span>6</span><span>7</span><span>8</span><span>9</span><span>10</span><span>11</span><span>12</span><span>13</span><span>14</span><span>15</span><span>16</span><span>17</span><span>18</span><span>19</span><span>20</span><span>21</span><span>22</span><span>23</span><span>24</span><span>25</span><span>26</span><span>27</span><span>28</span></span><code><span class="hljs-keyword">import</span> json

<span class="hljs-keyword">import</span> sqlalchemy
from sqlalchemy.orm <span class="hljs-keyword">import</span> sessionmaker

from models <span class="hljs-keyword">import</span> create_tables, Publisher, Shop, Book, Stock, Sale


DSN = <span class="hljs-string">'...'</span>
engine = sqlalchemy.create_engine(DSN)
create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

<span class="hljs-keyword">with</span> open(<span class="hljs-string">'fixtures/tests_data.json'</span>, <span class="hljs-string">'r'</span>) <span class="hljs-keyword">as</span> fd:
    <span class="hljs-keyword">data</span> = json.load(fd)

<span class="hljs-keyword">for</span> record <span class="hljs-built_in">in</span> <span class="hljs-keyword">data</span>:
    model = {
        <span class="hljs-string">'publisher'</span>: Publisher,
        <span class="hljs-string">'shop'</span>: Shop,
        <span class="hljs-string">'book'</span>: Book,
        <span class="hljs-string">'stock'</span>: Stock,
        <span class="hljs-string">'sale'</span>: Sale,
    }[record.get(<span class="hljs-string">'model'</span>)]
    session.add(model(id=record.get(<span class="hljs-string">'pk'</span>), **record.get(<span class="hljs-string">'fields'</span>)))
session.commit()
</code></pre>
<hr>
<h2><strong>Общие советы:</strong></h2>
<ul>
<li>Параметры подключения к БД следует выносить в отдельные переменные (логин, пароль, название БД и пр.)</li>
<li>Загружать значения лучше из окружения ОС, например через os.getenv()</li>
<li>Заполнять данными можно вручную или выполнить необязательное задание 3</li>
</ul>