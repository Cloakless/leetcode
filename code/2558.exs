defmodule Solution do
  @spec pick_gifts(gifts :: [integer], k :: integer) :: integer
  def pick_gifts(gifts, k) do
    if k == 0 do
      List.foldr(gifts, 0, fn(x, acc) -> x + acc end)
    else
      sorted = gifts |> Enum.sort(:desc)
      [head | tail] = sorted
      head = trunc(:math.sqrt(head))
      pick_gifts([head | tail], k-1)
    end
  end
end
