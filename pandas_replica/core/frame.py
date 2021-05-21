import numpy as np 

__version__ = '0.0.11111'

class DataFrame:
    def __init__(self, data):

        self._check_dict(data)
        self._check_array_length(data)

        self.data = data

    def _check_dict(self, data):
        if not isinstance(data, dict):
            raise ValueError('DataFrame constructor not properly called!')

    def _check_array_length(self, data):
        raw_lengths = [len(x) for x in data.values()]
        lengths = list(set(raw_lengths))
        if len(lengths) > 1:
            raise ValueError('arrays must all be same length')

    @property
    def columns(self):
        return list(self.data.keys())

    @property
    def shape(self):
        return (len(list(self.data.values())[0]), len(self.data))

    def _repr_html_(self):
        
        html = '<table><thead><tr><th></th>' # first <th> element is empty for our index column
        for col in self.columns:
            html += f"<th>{col}</th>" # then we populate the remaining <th> with our columns

        html += '</tr></thead><tbody>'

        for i in range(len(list(self.data.values())[0])):
            html += f'<tr><td><strong>{i}</strong></td>' # add the index
            for _, values in self.data.items():
                html += f'<td>{values[i]}</td>' # for each column, add array[i] value into <td>
            html += '</tr>'

        html += '</tbody></table>'
        return html
