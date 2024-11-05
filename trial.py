st = 'The Child component defines its own state variable data and a function handleClick that calls the sendDataToParent function passed down as a prop with the current value of data as an argument. The Child component renders an <input> element and a <button> element, and when the button is clicked, the handleClick function is called.'
max_pt = 5
print(
    list(st[i: i + max_pt] for i in range(0, len(st), max_pt))
)