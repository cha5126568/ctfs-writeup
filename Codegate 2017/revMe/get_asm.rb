iseq = nil
File.open("revMe", "rb") do |file|
  iseq = RubyVM::InstructionSequence.load_from_binary(file.read)
end
puts iseq.disasm