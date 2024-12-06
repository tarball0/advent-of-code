local function getNums(input)
	local num1, num2 = string.match(input, "(%d+)|(%d+)")
	return tonumber(num1), tonumber(num2)
end

local function getMiddleValue(arr)
    local length = #arr
    if length == 0 then
        return nil  -- Empty array
    end
    local middleIndex = math.floor(length / 2) + 1
    return arr[middleIndex]
end

local function split(inputstr, sep)
  if sep == nil then
    sep = "%s"
  end
  local t = {}
  for str in string.gmatch(inputstr, "([^"..sep.."]+)") do
    table.insert(t, tonumber(str))
  end
  return t
end


local function has_value (tab, val)
    for index, value in ipairs(tab) do
        if value == val then
            return true
        end
    end

    return false
end

----------------------------------------------------------------------

local file1 = io.open("inputp1.txt", "r")
local file2 = io.open("inputp2.txt", "r")
local reftable = {}
local update = {}
local finaltable = {}


for line in file1:lines() do
	local n1, n2 = getNums(line)
	if not reftable[n1] then
		reftable[n1] = {}
	end
	table.insert(reftable[n1], n2)
end

local c = 1
for line in file2:lines() do
	update = split(line, ",")
	local valid = true

	for index, value in ipairs(update) do
		local adjtable = reftable[value]
		if adjtable == nil then
			goto continue
		end
		for i = index, 1, -1 do
			if has_value(adjtable, update[i]) then
				valid = false
			end
		end


		::continue::
	end
	if valid then
		finaltable[c] = update
		c = c+1
	end
end

for _, upd in ipairs(finaltable) do
	for _, val in ipairs(upd) do
		io.write(val .. ",")
	end
	print()
end

local answer = 0
for _, val in ipairs(finaltable) do
	answer = answer + getMiddleValue(val)
end
print("answer " .. answer)

file1:close()
file2:close()
